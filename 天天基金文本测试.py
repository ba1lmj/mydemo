from urllib import request
import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')


xw_class=[]#空变量用来存类别
title=[]#用来存标题
for i in range(1, 40):#自定义函数
    resp = urllib.request.urlopen('http://roll.eastmoney.com/fund_'+str(i)+'.html')#获取网页
    html_data = resp.read().decode('utf-8')#读入数据
    soup = bs(html_data, 'html.parser')
    list = soup.find_all('div', class_='contain')#筛选网页中的div标签中的css为contain的节点
    xw = list[0].find_all('a')#找出a标签
    df = pd.DataFrame(columns=['class','title'])#建立一个包含class和title列的DataFrame
    for i in range(len(xw)):
        if i % 2 == 0:#偶数项分为类别，奇数项分为标题
            xw_class.append(xw[i].get_text())
        else:
            title.append(xw[i].get_text())

    df = pd.DataFrame({'类别':xw_class,'标题':title})#将分好的数据添加到df
    print(df)



