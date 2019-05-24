import tushare as ts
import stockstats #用来计算指标的包
from pyecharts.charts import EffectScatter#特效散点图

token="f609de55c27ef5c2caf2517a7fdcfdfcbd93112abbf525debe2ca363"# 初始化接口
ts.set_token(token)
pro=ts.pro_api()# 初始化接口
df2 =ts.pro_bar(pro_api=pro, ts_code='000001.SZ', start_date='20180101', end_date='20190101', ma=[5, 10, 30, 60])#获取2018年的股票数据
stockStat = stockstats.StockDataFrame.retype(df2)#初始化统计类




#print(stockStat['rsi_10'].tolist())#输出rsi_10这一列的数值
stockStat['rsi_5'].tolist()
stockStat['rsi_10'].tolist()
#print(df2[df2.rsi_5>79.5])#输出df2中rsi_5>79.5的行，并赋给rsi10_list
rsi10_list = df2[df2.rsi_5>79.5]
es = EffectScatter("散点图")
es.add("effectScatter",x_axis=rsi10_list['trade_date'],y_axis=rsi10_list['high'])#添加散点图的统计数据
es.render("00.html")#输出为00.html

