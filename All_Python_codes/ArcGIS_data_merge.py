import os
import arcpy
arcpy.env.workspace = "C:/Skydrive/2014 Ontodia/National/Census_tract/shapefiles/zips/tl_2013_06_tract"
path = os.listdir("C:/SkyDrive/2014 Ontodia/National/Census_tract/zips/tl_2013_06_tract/")#unzipped all shapefiles to thsi folder
shapefile = []
for i in path:
	suffix = ".shp";
	if i.endswith(suffix):#getting all files end with '.shp' to a new list
		shapefile.append(i)
arcpy.Merge_management(shapefile,"C:/SkyDrive/2014 Ontodia/National/Census_tract/shapefiles/merge")#the output folder should be a new folder that's not exited.