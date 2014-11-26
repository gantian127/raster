__author__ = 'jamy'

from osgeo import gdal
import os

# set working dir
work_dir = r"/Users/jamy/Desktop"
os.chdir(work_dir)

# set source file name and destination file name and file format
src_filename ='original_dem_arc_grid'
dst_filename = 'opt2_geotiff'
format = 'GTiff'

# Open existing dataset
src_ds = gdal.Open(src_filename)

# Open output format driver
driver = gdal.GetDriverByName(format)

# output to new format
dst_ds = driver.CreateCopy(dst_filename, src_ds, 0)

# Properly close the datasets to fush to d isk
dst_ds = None
src_ds = None