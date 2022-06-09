import requests
import re
import os
import time
from tkinter import *
def bizhan():
    ming0 = input("关键字：")
    ming1 = input(ming0 + ":要第几页内容：")
    ming4 = input("需要多少张呢:   ")
    ming2 = input("是否新建存储的目录：yes/no:    ")
    ming3 = input("请选择保存在哪个盘：c/d/f/e/r:    ")
    path1 = ming3 + ":\\老婆在这里"
    if ming2 == "yes":
        if os.path.exists(path1) == False:
            os.mkdir(path1)
            print("新建目录完成")
        else:
            print("新建目录已存在")
    url = "https://search.bilibili.com/article?keyword=%s" % ming0 + "&page=" + ming1
    ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
    reg1 = requests.get(url, headers=ua)
    reg1.encoding = reg1.apparent_encoding  # 自动解决乱码
    reg1.encoding = "utf-8"
    print(reg1)
    reg = reg1.text
    zz = re.findall(r'class="article-item"><a href="(.*?)"', reg)
    endless = 0

    namei = []
    name2 = []
    for lie in zz:
        i = "https:%s" % lie
        eg = requests.get(i, headers=ua).text
        ii = re.findall(r'<img data-src="(.*?)"', eg)

        for name in ii:
            if endless < int(ming4):
                endless += 1
                m = "https:" + name
                mi = ming0 + str(endless) + ".jpg"
                name1 = requests.get(m, headers=ua)
                namei.append(mi)
                with open(path1 + "/" + mi, "wb") as f:
                    f.write(name1.content)
                print(m, "----以缓存" + str(endless) + "张------")
                time.sleep(0.5)
    if len(namei) == 0:
        print("此页没你想要的内容")
    else:
        print("刚刚缓存了", namei)
        shan = input("(%s)" % path1 + "需要删除所有缓存吗，yes/no:   ")
        path = path1
        if shan == "yes":
            xianyou = os.listdir(path)
            for op in range(len(xianyou)):
                o = xianyou[op]
                i = "\\"
                os.remove(path + i + o)
            print("(%s)" % path1 + "文件已清空")
        elif shan == "no":
            print("感谢使用")
        print("路径————————(%s)" % path1)
bizhan()

#数据可视化






"""
for i in namei:
    ii = i
    name2.append(ii)
    name2.append("\n")
root = Tk()
text = Text(root)
text.pack()
text.insert(END, name2)
root.mainloop()
"""

