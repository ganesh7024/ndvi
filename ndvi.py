from osgeo import gdal
import numpy as np

def ndvi(red, nir):
 return ((nir - red)/(nir + red))
 
# Open each band using gdal
red_link = gdal.Open('.\data\img_data\T44QQE_20220919T044711_B04_10m.jp2')
nir_link = gdal.Open('.\data\img_data\T44QQE_20220919T044711_B08_10m.jp2')
 
# read in each band as array and convert to float for calculations
red = red_link.ReadAsArray().astype(np.float)
nir = nir_link.ReadAsArray().astype(np.float)

 
# Call the ndvi() function on red, NIR bands
ndvi2 = ndvi(red, nir)

# Create output filename based on input name 
outfile_name = 'TEST_NDVI.tif'
 
x_pixels = ndvi2.shape[0] # number of pixels in x
y_pixels = ndvi2.shape[1] # number of pixels in y
 
# Set up output GeoTIFF
driver = gdal.GetDriverByName('GTiff')
 
# Create driver using output filename, x and y pixels, # of bands, and datatype
ndvi_data = driver.Create(outfile_name,x_pixels, y_pixels, 1,gdal.GDT_Float32)
 
# Set NDVI array as the 1 output raster band
ndvi_data.GetRasterBand(1).WriteArray(ndvi2)
 
# Setting up the coordinate reference system of the output GeoTIFF
geotrans=red_link.GetGeoTransform() # Grab input GeoTranform information
proj=red_link.GetProjection() # Grab projection information from input file
 
# now set GeoTransform parameters and projection on the output file
ndvi_data.SetGeoTransform(geotrans) 
ndvi_data.SetProjection(proj)
ndvi_data.FlushCache()
ndvi_data=None





