#!/usr/bin/python3 
#coding=utf-8
from  PIL import Image,ImageColor
import os
i=1
j=1
os.chdir('/Users/evan/Pictures/tmp')
f="优王宣传册第二稿小_页面_01.png"
# f=input('拖入图片文件：')
# 头尾去空格
f=f.strip()
img=Image.open(f)
print(img.size)
img.show()