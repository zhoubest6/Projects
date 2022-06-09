import requests
import re
import time
ua = {
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
         }
url = "https://www.iqiyi.com/v_19rr7q5ado.html"
shuju = requests.get("https://z1.m1907.cn/?jx="+url)
print(shuju.text)
