# Test if gdal can store a raster as big tiff automatically when it exceeds the 4GB limit:

import gdal, ogr, osr, os, sys
import numpy as np

os.chdir(r'/Users/jamy/Dropbox/HS Specification/1 RDM specification/4 raster/raster_coding/create_test_raster')
rasterfn = 'floatn40w112_13.flt'
newRasterfn = 'big_tiff.tif'

# source raster data and metadata
raster = gdal.Open(rasterfn)
geotransform = raster.GetGeoTransform()
originX = geotransform[0]
originY = geotransform[3]
pixelWidth = geotransform[1]
pixelHeight = geotransform[5]
cols = raster.RasterXSize
rows = raster.RasterYSize
band = raster.GetRasterBand(1)
array = band.ReadAsArray()

# write source raster to output raster
driver = gdal.GetDriverByName('GTiff')
outRaster = driver.Create(newRasterfn, cols, rows, 7, gdal.GDT_Float32)
outRaster.SetGeoTransform((originX, pixelWidth, 0, originY, 0, pixelHeight))
outRasterSRS = osr.SpatialReference()
outRasterSRS.ImportFromWkt(raster.GetProjectionRef())
outRaster.SetProjection(outRasterSRS.ExportToWkt())

for i in range(1, 8):
    print 'create '+ str(i)+' layer'
    outRaster.GetRasterBand(i).WriteArray(array)
    outRaster.FlushCache()

outRaster = None

print 'finished'

