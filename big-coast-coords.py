import re

import geopandas
from shapely.geometry import Point


def process_row(row):
    """Parse copy/pasted BigCoast coords, stripping out all text lines"""
    try:
        coord = re.findall("\s([-0-9.]+\s[-0-9.]+)", row)[0]
        lat, lon = map(float, coord.split())
        record = {"point": Point(lon, lat)}
    except IndexError:
        record = None
    return record


if __name__ == "__main__":
    fname = "data/coords-by-line.txt"

    with open(fname) as f:
        records = [process_row(row) for row in f]
    points = [record["point"] for record in records if record]  # drops None

    point_gdf = geopandas.GeoDataFrame(geometry=points, crs="epsg:4326")
    point_gdf = point_gdf.to_crs("esri:102001")

    buffer = point_gdf.buffer(100, cap_style=3)  # cap_style=3 -> square edges
    geoms = buffer.unary_union
    buffered_gdf = geopandas.GeoDataFrame(geometry=[geoms], crs="esri:102001")
    buffered_gdf = buffered_gdf.explode()
    buffered_gdf = buffered_gdf.buffer(-50, cap_style=3)
    print(f"area in square meters: {buffered_gdf.area.sum():.2f}")

    buffered_gdf = buffered_gdf.to_crs("epsg:4326")
    buffered_gdf.to_file("/tmp/bigcoast-buffered.json", driver="GeoJSON")
