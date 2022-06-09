import numpy as np
from PIL import Image
import os
"""img = Image.open("E:\\Genshin Impact\\Genshin Impact Game\\ScreenShot\\202121173426.png")  # 打开图片
img1 = Image.open("E:\\Genshin Impact\\Genshin Impact Game\\ScreenShot\\2021210164422.png")
img2 = Image.open("E:\\Genshin Impact\\Genshin Impact Game\\ScreenShot\\2021728231328.png")
im = np.array(img)  # 转化为ndarray对象
im0 = np.array(img1)
im1 = np.array(img2)
i = np.concatenate((im, im0,im1), axis=0)  # 纵向拼接
#im2 = np.concatenate((im, im), axis=1)  # 横向拼接
# 生成图片
img1 = Image.fromarray(i)
#img2 = Image.fromarray(im2)
# 保存图片
img1.save('test1.jpg')
#img2.save('test2.jpg')"""

open_1 = "F:\\漫画"
open_21 = os.listdir(open_1)
open_21.sort(key= lambda x:int(x[:-4]))#listdir解决排序错乱
print(open_21)

for i in range(len(open_21)):
    value = open_21[i]
    #print(i)
    print(value)
    if i == i+3:
        print(i)


