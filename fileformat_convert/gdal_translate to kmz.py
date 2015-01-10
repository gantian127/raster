__author__ = 'jamy'

from osgeo import gdal
import os


def export_tif_to_kmz(raster_file_name):
    # Open existing dataset
    initial_raster = gdal.Open(raster_file_name)

    # Open output format driver
    format = 'KMLSUPEROVERLAY' # this specify the export file format
    driver = gdal.GetDriverByName(format)
    output_name = 'output.kmz'  # define to export as  .kmz or .kml

    # Output to storage format
    final_raster = driver.CreateCopy(output_name, initial_raster, 0)

