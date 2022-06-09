import requests,re,time,os函数

i = input('输入第几页：')
url = "https://pic.netbian.com/index_"+i+".html"
print(url)
urli = "https://pic.netbian.com"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
req = requests.get(url, headers=headers).text
print(req)
pic_url = re.findall('img src="(.*?)"', req)
print(pic_url)


for urls in pic_url:
    #print(urls)
    #拼接图片链接
    ui = urli + urls
    #print(ui)
    i = ui.split('/')[-1]
    #print(i)
    response = requests.get(ui,headers=headers)
    print(response)

    with open("f:\\图片"+'/'+i,"wb") as f:
       f.write(response.content)
    time.sleep(1)
