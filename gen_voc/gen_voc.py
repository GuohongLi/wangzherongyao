# -*- coding: utf-8 -*-
import cv2  
import sys
import os
import shutil

#build dir
'''
--VOC  
    --Annotations  
    --ImageSets  
      --Main  
      --Layout  
      --Segmentation  
    --JPEGImages  
    --SegmentationClass  
    --SegmentationObject  
'''
DataSetName="wangzherongyao2017"
if os.path.exists(DataSetName):
	shutil.rmtree(DataSetName)
os.makedirs(DataSetName +"/" + "Annotations")
os.makedirs(DataSetName +"/" + "ImageSets/Main")
os.makedirs(DataSetName +"/" + "ImageSets/Layout")
os.makedirs(DataSetName +"/" + "ImageSets/Segmentation")
os.makedirs(DataSetName +"/" + "JPEGImages")
os.makedirs(DataSetName +"/" + "SegmentationClass")
os.makedirs(DataSetName +"/" + "SegmentationObject")
#list input

