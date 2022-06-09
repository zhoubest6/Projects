import requests
import re
import time
import os

print(" https://pic.netbian.com/index  #首页")
print(" https://pic.netbian.com/4kfengjing/index  #风景")
print(" https://pic.netbian.com/4kmeinv/index  #美女")
print(" https://pic.netbian.com/4kyouxi/index  #游戏")
print(" https://pic.netbian.com/4kdongman/index  #动漫")
print(" https://pic.netbian.com/4kyingshi/index  #影视")
print(" https://pic.netbian.com/4kmingxing/index  #明星")
print(" https://pic.netbian.com/4kqiche/index  #汽车")
print(" https://pic.netbian.com/4kdongwu/index  #动物")
print(" https://pic.netbian.com/4krenwu/index  #人物")
print(" https://pic.netbian.com/4kmeishi/index  #美食")
print(" https://pic.netbian.com/4kzongjiao/index  #宗教")
print(" https://pic.netbian.com/4kbeijing/index  #背景")
diz = input("填上方对应地址：")
ua = {
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
         }
si = input("输入开始页数：")
si1 = int(si)
su = input("输入结尾页数：")
su1 = int(su)
delayed = input("嫌慢可以调延时，最佳为1：")
delayed1 = int(delayed)

si = "_"

while si1<su1:
     si1 += 1

     for jie1 in str(si1):

         url = diz + si + str(jie1) + ".html"
         req = requests.get(url, headers=ua).text
         pic_url = re.findall('img src="(.*?)"', req)
         req1 = requests.get(url, headers=ua).text
         obtain1 = re.findall('<li><a href="/tupian/(.*?)"', req1)  # html
         print(url)
         #print(pic_url)
         print(obtain1)


         for pic_url3 in obtain1:

             url2 = "https://pic.netbian.com/tupian/" + pic_url3
             obtain2 = requests.get(url2, headers=ua).text
             pic_url4 = re.findall('id="img"><img src="(.*?)"', obtain2)

             for url4 in pic_url4:
                 ui = "https://pic.netbian.com" + url4
                 i = ui.split('/')[-1]
                 response = requests.get(ui, headers=ua)
                 with open("f:\\图片" + '/' + i, "wb") as f:
                     f.write(response.content)
                 print(ui)

                 time.sleep(delayed1)

     print("-----第", si1, "页Cache_complete-----")

print("------Cache_complete(...)-------")




