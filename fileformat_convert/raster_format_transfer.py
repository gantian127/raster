"""
Module used to convert the raster file format for storage and export purpose in HydroShare.
"""
__author__ = 'Tian Gan'


import gdal
import rasterio
import os


def convert_raster_to_geotiff(raster_file_name):
    """
    (string)-> raster

    Return: raster file in Geotiff format
    """

    # Open existing dataset
    initial_raster = gdal.Open(raster_file_name)

    # Open output format driver
    driver = gdal.GetDriverByName('GTiff')

    # Set the final raster name as raster_name.tif
    final_raster_name = os.path.splitext(raster_file_name)[0]+'.tif'

    # Output to storage format
    final_raster = driver.CreateCopy(final_raster_name, initial_raster, 0)


def convert_raster_to_export_format(raster_file_name, raster_format_code):
    """
    (string)-> json string

    Return: raster file as the export format supported by HydroShare

    Note:
    1) Supported format name in HS and corresponding format code in GDAL lib (list as Name: Code)
    'Arc/Info ASCII Grid': 'AAIGrid', # work
    'ENVI': 'ENVI', # work
    'Arc/Info Binary Grid': 'AIG', # doesn't work
    'Erdas Imagine': 'EIR',  # doesn't work
    'USGS ASCII DEM': 'USGSDEM',  # work

    2) rasterio is a python lib for manipulation raster file which maybe considered another way for coding
    with raserio.drivers():
         rasterio.copy('logan.tif', 'logan',driver = 'ENVI')

    3) another way is to use the command directly call gdal_translate function through terminal using python code

    """

    # Open existing dataset
    initial_raster = gdal.Open(raster_file_name)

    # Open output format driver
    driver = gdal.GetDriverByName(raster_format_code)

    # Set the final raster name
    final_raster_name = os.path.splitext(raster_file_name)[0]

    # Output to storage format
    final_raster = driver.CreateCopy(final_raster_name, initial_raster, 0)