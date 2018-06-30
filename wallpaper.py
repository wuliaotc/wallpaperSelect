#!/usr/bin/python
#-*- coding:UTF-8 -*-

#python 3.7
from PIL import Image
import os
import shutil
import warnings

def enumFile(path):
	for root,dirs,files in os.walk(path):#枚举文件
		for name in files:#name为文件名
			str=os.path.join(root,name)#合并字符串
			temp=str.rfind('.')#定位'.'
			for ext in exts:
				if(str[temp+1:]==ext):
					ImageScreen(str)
					break
					

def ImageScreen(file):
	try:
		im=Image.open(file)
		width,length=im.size
		scale=float(width)/length
		if(scale<value*H_scale and scale>H_scale/value):
			if(width*length<H_width*H_length):
				shutil.copy(file,targetDir_Low)
			else:
				shutil.copy(file,targetDir)
	except :
		print('Error:'+file)


def mkdir(path):
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    Exists=os.path.exists(path)
 
    # 判断结果
    if not Exists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
 
        print (path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path+' 目录已存在')
        return False
#====setting=================

H_width=1920
H_length=1080
#设备分辨率
value=1.2
#筛选图片所用模糊比例
path=r'F:\壁纸'
#来源图片顶级目录
exts=('png','jpg','bmp')
#图片扩展名
targetDir=r'F:\\筛选'
#目标目录
targetDir_Low=r'F:\\筛选\\low'
#较低分辨率图片目录

H_scale=float(H_width)/H_length
#warnings.simplefilter('ignore', Image.DecompressionBombWarning)
#禁用image dos压缩炸弹警告

#============================
mkdir(targetDir)
mkdir(targetDir_Low)
enumFile(path)




