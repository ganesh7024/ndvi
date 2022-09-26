from osgeo import ogr
from osgeo import gdal


shapefile = "./data/india_2001_district.shp"
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 0)
layer = dataSource.GetLayer()
layer.SetAttributeFilter("DISTRICT = 'Visakhapatnam'")
for feature in layer:
    geom=feature.GetGeometryRef()
    extent = geom.GetEnvelope()
    ex = list(extent)
    ex[1], ex[2] = ex[2], ex[1]
    print(ex)
  






