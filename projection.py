# -*- coding: utf-8 -*-
### arcpy로 좌표변환하기
import arcpy

# 좌표변환 할 shp파일 변수
input_features = r'C:\WORK\Arcpy_study\Arcpy_jibeon\AL_11_D002_20230902.shp'

# output파일 변수 설정
output_feature_class = r'C:\WORK\Arcpy_study\Arcpy_jibeon\AL_11_D002_20230902_project.shp'

# 변환하고자 하는 좌표계 변수 설정
out_coordinate_system = arcpy.SpatialReference('WGS 1984')

# run the tool
arcpy.Project_management(input_features, output_feature_class, out_coordinate_system)