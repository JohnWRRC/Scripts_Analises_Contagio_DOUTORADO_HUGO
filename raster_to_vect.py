import arcpy
from arcpy import env
#0500
env.workspace=r'F:\data\Hugo\DB_2015_02_d18\Buffer_0500m\Cut_Maps_0500m'
rt=arcpy.ListRasters()
env.workspace=r'F:\data\Hugo\DB_2015_02_d18\Buffer_0500m\Cut_Maps_0500m_SHP'
for i in rt:
    out=i.replace('.tif','_shp')
    arcpy.RasterToPolygon_conversion(i,out,"NO_SIMPLIFY","Value")

#1500
env.workspace=r'F:\data\Hugo\DB_2015_02_d18\Buffer_1500\Cut_Map_1500m'
rt=arcpy.ListRasters()
env.workspace=r'F:\data\Hugo\DB_2015_02_d18\Buffer_1500\Cut_Maps_1500m_SHP'
for i in rt:
    out=i.replace('.tif','_shp')
    arcpy.RasterToPolygon_conversion(i,out,"NO_SIMPLIFY","Value")
    
#1500
env.workspace=r'F:\data\Hugo\DB_2015_02_d18\buffer_2000\Cut_Map_2000m'
rt=arcpy.ListRasters()
env.workspace=r'F:\data\Hugo\DB_2015_02_d18\Buffer_1500\Cut_Maps_2000m_SHP'
for i in rt:
    out=i.replace('.tif','_shp')
    arcpy.RasterToPolygon_conversion(i,out,"NO_SIMPLIFY","Value")
    
    


