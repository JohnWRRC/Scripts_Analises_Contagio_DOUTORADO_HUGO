import arcpy
from arcpy import env
#1000
env.workspace='F:\data\Hugo\DB_2015_02_d18\Buffer_1000m\split_buffer_vazio'
fc=arcpy.ListFeatureClasses()
inputMask='mapa_final_int.tif'
env.workspace=r'F:\data\Hugo\DB_2015_02_d18\Buffer_1000m\Cut_Maps'
for i in fc:
    mask=i.replace('.shp','')
   
    output_Mask=mask+'_extract_buff_1000.tif'
    output_Mask=output_Mask.replace('__','_')
    arcpy.gp.ExtractByMask_sa(inputMask, mask, output_Mask)


#500
env.workspace='F:\data\Hugo\DB_2015_02_d18\Buffer_0500m\split_buffer_vazio'
fc=arcpy.ListFeatureClasses()
inputMask='mapa_final_int.tif'
env.workspace=r'F:\data\Hugo\DB_2015_02_d18\Buffer_0500m\Cut_Maps'
for i in fc:
    mask=i.replace('.shp','')
   
    output_Mask=mask+'_extract_buff_0500.tif'
    output_Mask=output_Mask.replace('__','_')
    arcpy.gp.ExtractByMask_sa(inputMask, mask, output_Mask)
    
    
    
    
    
    
#1500
env.workspace='F:\data\Hugo\DB_2015_02_d18\Buffer_1500\split_buff_vazio'
fc=arcpy.ListFeatureClasses()
inputMask='mapa_final_int.tif'
env.workspace=r'F:\data\Hugo\DB_2015_02_d18\Buffer_1500\Cut_Map'
for i in fc:
    mask=i.replace('.shp','')
   
    output_Mask=mask+'_extract_buff_1500.tif'
    output_Mask=output_Mask.replace('__','_')
    arcpy.gp.ExtractByMask_sa(inputMask, mask, output_Mask)
    
    
    
#2000
env.workspace=r'F:\data\Hugo\DB_2015_02_d18\buffer_2000\split_buff_vazio'
fc=arcpy.ListFeatureClasses()
inputMask='mapa_final_int.tif'
env.workspace=r'F:\data\Hugo\DB_2015_02_d18\buffer_2000\Cut_Map'

for i in fc:
    mask=i.replace('.shp','')
    
    output_Mask=mask+'_extract_buff_2000.tif'
    output_Mask=output_Mask.replace('__','_')
    arcpy.gp.ExtractByMask_sa(inputMask, mask, output_Mask)

