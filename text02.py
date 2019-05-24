from urllib import request
import urllib.request
from bs4 import BeautifulSoup as bs
import re
import jieba  # 分词包
import pandas as pd
import numpy
import matplotlib
jieba.load_userdict("D:\Fina_dic.txt")
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
from matplotlib import pyplot as plt
import matplotlib
from wordcloud import WordCloud  # 词云包
from scipy.misc import imread


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')


news = ''
for i in range(1, 97):
    resp = urllib.request.urlopen('http://roll.eastmoney.com/finance%2Cbond%2Cfund%2Cstock%2Chk_'+str(i)+'.html')
    html_data = resp.read().decode('utf-8')
    soup = bs(html_data, 'html.parser')
    list = soup.find_all('div', class_='contain')
    xw = list[0].find_all('a')
    print(xw)
    for i in range(len(xw)):
        title = xw[i].get('title')
        if title is None:
            news = news + '。'
        else :
            news = news + (title)
            print(xw[i].get('title'))



#print(news)
#     resp2 = request.urlopen(link)
#     html_data2 = resp2.read().decode('utf-8')
#     soup2 = bs(html_data2, 'html.parser')
#     contents_list = soup2.find_all('div', class_='text_content')
#     # print(contents_list)
#     content = contents_list[0].find_all('p')
#     for i in content:
#         news += i.get_text().replace(' ','')
#
#
# # print(news)
segment = jieba.lcut(news)
words_df = pd.DataFrame({'segment': segment})
print(segment)
stopwords = pd.read_csv("D:\stopwords2.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],
                        encoding='gb18030')  # quoting=3全不引用
words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
print(words_df)

# 利用numpy计算包进行词频统计
words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": numpy.size})
words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)
print(words_stat.head())

# image = imread("3.jpg")
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80)
word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}
wordcloud = wordcloud.fit_words(word_frequence)
plt.imshow(wordcloud)
plt.show()