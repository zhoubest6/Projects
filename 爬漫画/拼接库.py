import requests,re,os
import numpy as np
from PIL import Image

iy = 0
open = os.listdir("f:\\漫画")
open.sort(key=lambda x:int(x[:-4]))
#print(open)
while True:
    if iy == iy:
        iy+=1
        ming = str(iy)
        ming1 = iye
        img = Image.open("f:\\漫画\\%s"%ming+".jpg")
        print("1")
        print(ming1)
        #img = Image.open("f:\\漫画\\1.jpg")
        img1 = Image.open("f:\\漫画\\%s"%ming+".jpg")
        print("2")
        print(ming1+1)
        img2 = Image.open("f:\\漫画\\%s"%ming+".jpg")
        print("3")
        print(ming1+1)
        im,im1,im2 = np.array(img),np.array(img1),np.array(img2)
        i1 = np.concatenate((im, im1, im2), axis=0)
        img1.save('拼接1.jpg')
        print("第一张完成——————%s"%ming)
        img = Image.open("f:\\漫画\\4.jpg")
        img1 = Image.open("f:\\漫画\\5.jpg")
        img2 = Image.open("f:\\漫画\\6.jpg")
        im, im1, im2 = np.array(img), np.array(img1), np.array(img2)
        i2 = np.concatenate((im, im1, im2), axis=0)
        img1.save('拼接2.jpg')


