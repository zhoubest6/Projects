import requests
import pyttsx3
from tkinter import *
import xlsx_ku.biaoge  as biaoge
from lxml import etree

class xiao_shuo():
    def __init__(self):

        self.url = "https://www.qidian.com/all/"
        self.ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
        self.fen_li=[]#小说分类的url
        self.name = []#小说的分类
        self.data = {}#分类名称和url
        self.urli=[]
        self.fen_li_he = []  # 合成说分类的url
        self.zhongjie = 0  #免费的章节数量
        self.url1=[]
        self.url1_1=[]  #合成章节的URL
        self.cha=[]

    def fenli_url(self):
        reg = requests.get(self.url, headers=self.ua)
        reg.encoding = reg.apparent_encoding  # 自动解决乱码
        reg.encoding = "utf-8"
        fen_li_url = re.findall(r'class=""><a href="(.*?)"', reg.text)  # 小说分类
        fen_li_url_ming = re.findall(r'data-eid="qd_B(.*?)<cite>', reg.text)
        fen_li_url = fen_li_url[:15]
        for i in range(len(fen_li_url)):
            self.fen_li.append("https:" + fen_li_url[i])
        xa = fen_li_url_ming[0][582:]
        fen_li_url_ming[0] = xa
        for i in fen_li_url_ming:
            self.name.append(i[4:])
        for i in range(len(self.name)):
            self.data[self.name[i]] = str(self.fen_li[i])
        return self.fen_li,self.name,self.data

    def fenliurl_hec(self):
        for i in range(len(self.fen_li)):
            self.fen_li_he.append(self.fen_li[i])

    def zhu_ye(self):
        y = input("输入小说的类别：")
        url = self.data[y]
        reg = requests.get(url, headers=self.ua)
        reg.encoding = reg.apparent_encoding  # 自动解决乱码
        reg.encoding = "utf-8"
        li_url = re.findall(r'<div class="book-mid-info"> <h2><a href="(.*?)"', reg.text)
        novel_title = re.findall(r'alt="(.*?)在线阅读"', reg.text)  # 小说名
        for i in range(len(li_url)):
            self.urli.append("https:" + li_url[i] + "#Catalog")
            self.data[novel_title[i]] = "https:" + li_url[i] + "#Catalog"
            print("小说名:", novel_title[i])  # 获取小说名

    def zhiangjie_neirong(self):
        global ze
        ze = input("输入已有的小说名:")
        for i in range(1):
            url = self.data[ze]
            reg = requests.get(url, headers=self.ua)
            reg.encoding = reg.apparent_encoding  # 自动解决乱码
            reg.encoding = "utf-8"
            Html = etree.HTML(reg.text)
            result = Html.xpath(r'/html/body/div[1]/div[6]/div[3]/div[2]/div[2]/ul/li/h2/*/@href')
            print(result)

            # ai = re.findall(r'target="_blank" data-eid="qd_G55" data-cid="(.*?)"', reg.text)
            # print(ai)
            a1 = re.findall(r'</i>共(.*?)章<span class=free> 免费</span>', reg.text)
            print(int(a1[-1]))
            if len(a1)>=2:
                self.zhongjie = int(a1[-1])
            else:
                self.zhongjie = int(a1[0])
            self.url1 = result[0:-1]

    def zhangjie_url_he(self):
        for i in range(len(self.url1)):
            self.url1_1.append("https:" + self.url1[i])
    # https://read.qidian.com/chapter/s8jssYMfwMbhI-Ha6N4TBg2/9phQvALALFm2uJcMpdsVgA2
    def neirong(self):
        global zhongjie
        zhongjie=self.zhongjie-1
        # for i in range(5):
        for i in range(0,zhongjie):
            url = self.url1_1[i]
            reg = requests.get(url, headers=self.ua)
            reg.encoding = reg.apparent_encoding  # 自动解决乱码
            reg.encoding = "utf-8"
            # nei= re.findall(r'<p>(.*?)<p>', reg.text)
            nei = re.findall(r'window.cContent = "(.*?)"', reg.text)
            nei= "".join(nei).split("&lt;p&gt;")[1:-1]
            print(i,nei)
            self.cha.append(nei)
            ao = i + 1
            print("第%s章" % ao, "————————————————————完成————————————————————————")  # 打印内容

        return self.cha

    def yu_ying(self,data):#语音播报
        tts=pyttsx3.init()
        # tts.setProperty("rate",200)#默认200，控制语速
        tts.getProperty("voices")
        rate = tts.getProperty('rate')
        tts.setProperty('rate', rate-50)
        tts.say(data)
        tts.runAndWait()
        tts.stop()


if __name__ == '__main__':
    path = "data.xlsx"
    biaoge.shan_chu(path)
    x1=xiao_shuo()
    print("小说类型：","（"," - ".join(x1.fenli_url()[1]),"）")
    x1.fenliurl_hec()
    x1.zhu_ye()
    x1.zhiangjie_neirong()
    x1.zhangjie_url_he()

    #文本内容写入excel
    data = x1.neirong()
    data1=data[0]
    #print(len(data1[0]))
    for i in range(len(data)):
        biaoge.xie(path, data[i])

    #读出文件加入语音播报
    x2= biaoge.du(path)
    s2="".join(x2)
    kaitou="__________免费章节只有{}章,正在为您读的小说是{}__________".format((zhongjie-1),ze)
    print(kaitou)
    x1.yu_ying(kaitou)
    for i in x2:
        print(i)
        x1.yu_ying(i)


