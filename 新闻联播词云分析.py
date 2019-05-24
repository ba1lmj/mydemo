from urllib import request
from bs4 import BeautifulSoup as bs
import re
import jieba  # 分词包
import pandas as pd
import numpy
import matplotlib

matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
from matplotlib import pyplot as plt
import matplotlib
from wordcloud import WordCloud  # 词云包
from scipy.misc import imread

resp = request.urlopen('http://www.xwlbo.com/txt.html')#请求打开网址
html_data = resp.read().decode('utf-8')#读取网页中的内容
soup = bs(html_data, 'html.parser')  #创建 beautifulsoup 对象

xwlist = soup.find_all('ol', class_='xwlist')#对所有得到的网页中筛选出ol标签和class_='xwlist'的节点
xw = xwlist[0].find_all('a') #对xwlist的第0行筛选出标签为a的节点
num = xw[0].get('id')#在上一步的基础上取得所有的id的数目
#print(num[1:])#输出第一行之后所有数据
news = ''
for i in range(1,90):
    link = 'http://www.xwlbo.com/'+str(int(num[1:])-i)+'.html'#取新闻网页
    # print(link)#输出具体新闻网址
    resp2 = request.urlopen(link)#打开并传给一个变量
    html_data2 = resp2.read().decode('utf-8')#读入数据
    soup2 = bs(html_data2, 'html.parser')#创建一个bs对象
    contents_list = soup2.find_all('div', class_='text_content')#选择标签为div且CSS为class_='text_content'的节点
    # print(contents_list)
    content = contents_list[0].find_all('p')#在上一步的基础上选择P标签
    for i in content:
        news += i.get_text().replace(' ','')#取出p便签中的具体内容，并去掉空格


print(news)
segment = jieba.lcut(news)#对news进行分词处理
words_df = pd.DataFrame({'segment': segment})# 去掉停用词
print(segment)
stopwords = pd.read_csv("D:\chineseStopWords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],
                        encoding='gb18030')  # quoting=3全不引用  引入停用词文件
words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
print(words_df)

# 利用numpy计算包进行词频统计
words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": numpy.size})#对每一个segment进行数据统计
words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)#根据次数按照降序的方式重设索引
print(words_stat.head())#输出前五了频率最高的词

#image = imread("捕获.JPG")#取例图的形状
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)#设置图的尺寸
wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80)#设置词云的属性
word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}#词频分析
wordcloud = wordcloud.fit_words(word_frequence)#按照词频来生成图
plt.imshow(wordcloud)#显示图片
plt.show()