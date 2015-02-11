# Test if a raster can have different x width and y width value for a cell: Yes
# Test if a raster can have multiple bands with different data type: No

import gdal
import osr
import numpy


# define a geotiff driver
format = "GTiff"
driver = gdal.GetDriverByName(format)

# define raster dataset
dst_filename = 'test_band_data_type.tif'
dst_ds = driver.Create(dst_filename, 512, 512, 2)

# set projection info
dst_ds.SetGeoTransform([444720, 30, 0, 3751320, 0, -25])  # set x, y cell width as 30, 25
srs = osr.SpatialReference()
srs.SetUTM(11, 1)
srs.SetWellKnownGeogCS('NAD27')
dst_ds.SetProjection(srs.ExportToWkt())


# write data to raster band and set no data value
raster1 = numpy.zeros((512, 512), dtype=numpy.uint8)
dst_ds.GetRasterBand(1).WriteArray(raster1)

raster2 = numpy.ones((512, 512), dtype=numpy.uint8)
dst_ds.GetRasterBand(2).WriteArray(raster2)


## close properly the dataset
dst_ds = None

