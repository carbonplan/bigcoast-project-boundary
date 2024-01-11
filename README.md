<p align="left" >
<a href='https://carbonplan.org'>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://carbonplan-assets.s3.amazonaws.com/monogram/light-small.png">
  <img alt="CarbonPlan monogram." height="48" src="https://carbonplan-assets.s3.amazonaws.com/monogram/dark-small.png">
</picture>
</a>
</p>

# carbonplan / bigcoast-project-boundary

## context

data and code used to reconstruct an approximation of the boundary of the BigCoast offset project, which underlie a [blog post](https://carbonplan.org/blog/bigcoast-project-boundary) we wrote about the project.


## methods

we first copy/pasted the raw coordinates contained within `VCS_Joint_Prjct_Description_Monitoring_Report_BigCoast.pdf`, an official project document uploaded to the Verra offset registry. we then used a series of command line tools, like `awk` and `tr`, to create `coords-by-line.txt`. from there, we used we used the Python libraries `geopandas` and `shapely` to further process the data. the transformations are all contained within `big-coast-coords.py`. 

to reduce the size of the resulting GeoJSON file, we used [mapshaper](https://github.com/mbloch/mapshaper) to produce a simplified geometray: 

```
mapshaper /tmp/bigcoast-buffered.json -simplify dp 15% -o precision=0.0001 /tmp/bigcoast-simplified.json
```


## about us

CarbonPlan is a nonprofit organization that uses data and science for climate action. We aim to improve the transparency and scientific integrity of climate solutions with open data and tools. [Find out more at carbonplan.org](https://carbonplan.org/) or get in touch by [opening an issue](https://github.com/carbonplan/extreme-heat/issues/new) or [sending us an email](mailto:hello@carbonplan.org).
