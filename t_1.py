from pyecharts import Pie,Page,Line,ThemeRiver,Bar,HeatMap,Overlap,Grid,Radar
from pyecharts import Scatter3D
import numpy as np
import pandas as pd
from pyecharts import configure
from random import randint
from pyecharts_javascripthon.dom import window


attr1 = ["ShippingChina Co.", "(foreign capital) Schroeder Investment management Ltd", "Bank of Communications"]
v1 = [1000, 6000, 13000]
pie1 = Pie("Shareholder shareholding information",title_pos='center',title_text_size=24)
pie1.add("", attr1, v1, is_legend_show=False,radius=[15, 30],
         is_label_show=True,label_pos='inside',label_text_size=20)

attr2 = ["博士", "硕士", "本科"]
v2 = [30, 118, 5]
pie2 = Pie("基金经理学历组成",title_pos='center',title_top='15%',)
pie2.add("", attr2, v2, legend_orient='vertical',legend_top='15%',legend_pos='60%',radius=[30, 50],
         )



gm = pd.read_csv('C:/Users/Administrator/Desktop/公司规模变化.csv',encoding='GB2312')
# attr3 = gm.columns.values.tolist()
# print(gm)
# v3 = [30, 118, 5]
# line1 = Line("公司净资产规模变化")
# for i in range(2,len(attr3)):
#     line1.add(['全部','开放式','股票型','混合型','债券型','货币市场型','保本型','QDII'],gm,is_fill=True,
#                 line_opacity=0.8,area_opacity=0.4,symbol=None)
# v3 =  np.array(gm)
# v3_list = v3.tolist()
# print(v3_list)
# tr = ThemeRiver("公司净资产规模变化")
# tr.add(['全部','开放式','股票型','混合型','债券型','货币市场型','保本型','QDII'],v3_list , is_label_show=True)

attr3 = gm.columns.values.tolist()
bar1 = Bar("公司规模变化",subtitle='净资产',width=400)
for i in range(4,len(attr3)):
    bar1.add(attr3[i],gm['截止日期'],gm[attr3[i]],is_stack = True,
             legend_top='5%')  #is_stack = True才表示堆叠在一起

date = ['2017-12-31','2018-03-31','2018-06-30','2018-09-30','2018-12-31']
zcpz_1 =[19.43,18.70,19.79,19.62,18.25]
zcpz_2 =[44.93,47.73,54.15,55.98,61.28]
zcpz_3 =[21.06,30.14,20.52,17.63,17.99]
zcpz_4 =[1362.09,1563.74,1694.40,1564.15,1547.48]




bar2 = Bar("公司资产配置",subtitle='单位：%',width=400)
bar2.add('股票占净比',date,zcpz_1,yaxis_min=0,yaxis_max=80,legend_top='5%')
bar2.add('债券占净比',date,zcpz_2,yaxis_min=0,yaxis_max=80,legend_top='5%')
bar2.add('现金占净比',date,zcpz_3,yaxis_min=0,yaxis_max=80,legend_top='5%')

line1 = Line("",width=400)
line1.add('净资产（亿元）',date,zcpz_4,line_opacity=1,line_width=5,
          yaxis_min=1200,yaxis_max=2000,legend_top='10%')

overlap1 = Overlap(width=400)
overlap1.add(bar2)
overlap1.add(line1,yaxis_index=1,is_add_yaxis=True)



attr4 = ['制造业','信息技术服务业','房地产业','卫生和社会工作','文体娱乐业',
        '金融业','科学研究服务业','批发零售业','物流邮政业','采矿业']
v3 = [6.6,3.45,1.96,1.38,1.38,
      1.25,0.65,0.37,0.36,0.23]
bar3 = Bar('公司行业配置',width=400,subtitle='单位：%',)
bar3.add('占公司净值比例',attr4,v3,label_color=['#2F4F4F'],
         xaxis_interval=0, xaxis_rotate=30, yaxis_rotate=0,legend_top='10%')

category = ['近6月','近1年','近3年','近5年']
gpx1_1=[16.03,-7.34,20.28,64.74,]
gpx1_2=[14.69,-7.51,18.73,76.06]
gpx_hs300=[15.51,-8.57,24.39,76.42]
gpx2_1=[12.74,11.02,55.70,299.04]
gpx2_2=[10.17,-2.66,16.44,65.59]
gpx3_1=[3.93,6.36,6.76,12.12]
gpx3_2=[3.98,5.73,9.02,41.40]
gpx3_3=[2.97,5.71,1.03,22.63]

bar4 = Bar("公司股票型基金平均收益率",subtitle='单位：%',width=400)
bar4.add('该公司',category,gpx1_1,legend_top='10%')
bar4.add('同类平均',category,gpx1_2,legend_top='10%')
bar4.add('沪深300',category,gpx_hs300,legend_top='10%')

bar5 = Bar("公司混合型基金平均收益率",subtitle='单位：%',width=400)
bar5.add('该公司',category,gpx2_1,legend_top='10%')
bar5.add('同类平均',category,gpx2_2,legend_top='10%')
bar5.add('沪深300',category,gpx_hs300,legend_top='10%')


bar6 = Bar("公司债券型基金平均收益率",subtitle='单位：%',width=400)
bar6.add('该公司',category,gpx3_1,legend_top='10%')
bar6.add('同类平均',category,gpx3_2,legend_top='10%')
bar6.add('全债指数',category,gpx3_3,legend_top='10%')



heatx_axis = ["价值", "平衡", "成长"]
heaty_axis = ["大盘", "中盘", "小盘"]
data = [[0,0,3.28],[0,1,3.09],[0,2,26.86],
        [1,0,1.22],[1,1,1.75],[1,2,15.23],
        [2,0,2.15],[2,1,4.72],[2,2,40.99]]
heatmap = HeatMap('股票投资风格箱',subtitle='2：大盘\n1：中盘\n0:小盘',width=300,height=400)
heatmap.add(
    "",
    heatx_axis,
    heaty_axis,
    data,
    is_visualmap=True,
    visual_range=[0,50],
    visual_range_color=[ '#ffffff', '#22A6A5','#022921'],
    visual_text_color="#000",
    visual_orient="horizontal",
)

grid = Grid(width=400)
grid.add(pie1,grid_top="10%", grid_bottom="10%",grid_left="5%")
grid.add(pie2,grid_top="10%", grid_bottom="10%",grid_right="5%")


value1 = [[48.53,14.84,31.49,35.05,7.43]]
value2 = [[142.36,19.29,31.07,30.73,1.01]]
#用于调整雷达各维度的范围大小
c_schema= [{"name": "持股市盈率", "max": 200, "min": 0},
           {"name": "持股市净率", "max": 100, "min": 0},
           {"name": "股票集中度", "max": 100, "min": 0},
           {"name": "行业集中度", "max": 70, "min": 0},
           {"name": "投资集中度", "max": 10, "min": 0}]


radar = Radar("",title_pos='center')
radar.config(c_schema=c_schema,radar_text_size=20)
radar.add("交银", value1, item_color='#0A5E59',legend_orient='vertical',legend_pos='65%',
         legend_text_size=20,
          symbol=None,area_color= '#0A5E59', area_opacity=0.5,
          is_legend_show=False,line_width=3,background='C:/Users/Administrator/Desktop/molv.jpg')
radar.add("基金业", value2, item_color=' #0E867F',area_color='#0E867F',legend_orient='vertical',legend_pos='65%',
         legend_text_size=20,
           area_opacity=0.1,
          line_width=2)
heatx_axis = ["价值", "平衡", "成长"]
heaty_axis = ["大盘", "中盘", "小盘"]
data = [[0,0,0],[0,1,0],[0,2,0],
        [1,0,0],[1,1,0],[1,2,5],
        [2,0,2.8],[2,1,46.2],[2,2,42.4]]

heatmap1 = HeatMap('基金经理股票投资风格箱',subtitle='2：大盘\n1：中盘\n0:小盘')
heatmap1.add(
    "",
    heatx_axis,
    heaty_axis,
    data,
    is_visualmap=True,
    visual_range=[0,50],
    visual_range_color=[ '#ffffff', '#22A6A5','#022921'],
    visual_text_color="#000",
    visual_orient="horizontal",
)

page = Page()
page.add(pie1)
page.add(pie2)
page.add(grid)
page.add(bar1)
page.add(overlap1)
page.add(bar3)
page.add(bar4)
page.add(bar5)
page.add(bar6)
page.add(radar)

page.add(heatmap)
# page.add(rsi_line)
page.render(path='C:/Users/Administrator/Desktop/t_1.html')



