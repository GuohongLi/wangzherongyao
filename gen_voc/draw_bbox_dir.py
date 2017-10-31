# -*- coding: utf-8 -*-
import cv2
import sys
import os

indir = sys.argv[1]
outdir = sys.argv[2]
for filename in os.listdir(indir):
	filepath = os.path.join(indir,filename)
	img = cv2.imread(filepath)
	sp = img.shape
	x_cen=sp[1]/2
	y_cen=sp[0]/2
	w=sp[1]/9#10
	h=sp[0]/4#5
	x_min=x_cen-w/2
	y_min=y_cen-h/2
	x_max=x_cen+w/2
	y_max=y_cen+h/2
	# 画矩形框
	cv2.rectangle(img, (x_min,y_min), (x_max,y_max), (0,255,0), 4)
	# 标注文本
	#font = cv2.FONT_HERSHEY_SUPLEX
	#text = '001'
	#cv2.putText(img, text, (212, 310), font, 2, (0,0,255), 1)
	cv2.imwrite('%s/%s_new.jpg' % (outdir, filename), img)
