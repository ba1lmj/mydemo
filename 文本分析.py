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

news = ''

# print(news)
segment = jieba.lcut(news)
words_df = pd.DataFrame({'segment': segment})
print(segment)
stopwords = pd.read_csv("D:\stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],
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