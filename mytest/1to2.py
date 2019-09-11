#!/usr/bin/python3 
#coding=utf-8
from  PIL import Image,ImageColor
import os
i=1
j=1
os.chdir('/Users/evan/Pictures/tmp')
# os.chdir('/Users/evan/Downloads')
# f="优王宣传册第二稿小_页面_01.png"
# f="test1.png"
num=input("编号:")
num_n=str(int(num)+1)
f=input('拖入图片文件：')
# 头尾去空格
f=f.strip()
img=Image.open(f)
img=img.convert("RGB")
def _1to2():
    global img
    width,height=img.size
    img1=Image.new('RGB',(width//2,height),'white')
    img2=Image.new('RGB',(width//2,height),'white')
    print(img1.size)
    print(img2.size)
    for i in range(0,(width//2)*2):
        for j in range(0,height):
            data=(img.getpixel((i,j)))
            # print(data)
            if(i<width//2):
                img1.putpixel((i,j),(data[0],data[1],data[2]))
                pass
            else:
                img2.putpixel((i-width//2,j),(data[0],data[1],data[2]))
        print(i,width)
    img1.save("/Users/evan/Pictures/tmp1/优王宣传册"+num+".png")
    img2.save("/Users/evan/Pictures/tmp1/优王宣传册"+num_n+".png")
    print("保存成功")
_1to2()
# print(img.size)
