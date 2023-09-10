# -*- coding: utf-8 -*-
# 한글 인코딩 오류로 utf-8로 인코딩 선언
import arcpy

# 생성 경로, gdb이름
arcpy.CreateFileGDB_management("C:\WORK\Arcpy_study", "testgdb2")