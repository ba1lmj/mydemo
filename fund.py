from pyecharts.charts import Boxplot,Radar,HeatMap,Page,Bar,Line,Pie
import numpy as np
import pandas as pd
import pyecharts

attr3 = ['2016年中报','2016年年报','2017年中报','2017年年报','2018年中报']
cy1=[88.73,91.33,98.62,99.66,99.62]
cy2=[11.27,8.67,1.38,0.34,0.38]
cy3=[0.07,0.08,0.09,0.02,0.01]
barcy = Bar("持有比例",subtitle='单位：%',width=400)
barcy.add('个人持有比例',attr3,cy1,is_stack = True,
             legend_top='5%')  #is_stack = True才表示堆叠在一起
barcy.add('机构持有比例',attr3,cy2,is_stack = True,
             legend_top='5%')
barcy.add('员工持有比例',attr3,cy3,is_stack = True,
             legend_top='5%')

x_name = ['2016年一季报','2016年中报','2016年三季报','2016年年报','2017年一季报','2017年中报','2017年三季报','2017年年报','2018年一季报','2018年中报','2018年三季报']
gm_1 =[3.65,3.63,3.62,3.76,3.42,3.05,3.32,2.80,2.65,2.58,2.34]
line = Line("期末净资产(M)")
line.add(
    "",
    x_name,
    gm_1,
    is_fill=True,
    line_opacity=0.2,
    area_opacity=0.4,
    symbol=None,
)

date = ['股票','债券','现金','其他']
zcpz_1 =[75.64,6.09,7.72,10.56]
zcpz_2 =[52,20.6,17.29,9.96]
bar1 = Bar("资产配置",subtitle='单位：%',width=400)
bar1.add('交银成长混合A',date,zcpz_1,yaxis_min=0,yaxis_max=80,legend_top='5%')
bar1.add('同类平均',date,zcpz_2,yaxis_min=0,yaxis_max=80,legend_top='5%')

attr1 = ["制造业", "运输业", "房地产业", "采矿业", "金融业", "科学服务业", "卫生和社会工作", "其他"]
v1 = [41.57, 11.03, 7.82,7.08,4.76,3.49,0.49,23.76]
pie1 = Pie("行业投资占比",title_pos='center',width=400)
pie1.add("", attr1, v1, is_legend_show=False,radius=[15, 30],
         is_label_show=True,label_pos='outside')

year1 = ["2014", "2015", "2016", "2017", "2018"]
date = ['股票','债券','现金','其他']
pm_1 =[75.64,6.09,7.72,10.56]
pm_2 =[52,20.6,17.29,9.96]
bar2 = Bar("资产配置",subtitle='单位：%',width=400)
bar2.add('交银成长混合A',date,zcpz_1,yaxis_min=0,yaxis_max=80,legend_top='5%' )

value1 = [[45.45,37.78,20,35.56,26.67,6.67]]
value2 = [[27.27,55.56,13.33,60,57.78,57.78]]
#用于调整雷达各维度的范围大小
c_schema= [{"name": "阿尔法评分", "max": 100, "min": 0},
           {"name": "择时能力评分", "max": 100, "min": 0},
           {"name": "夏普比率评分", "max": 100, "min": 0},
           {"name": "稳定能力评分", "max": 100, "min": 0},
           {"name": "下行风险评分", "max": 100, "min": 0},
           {"name": "最大回撤评分", "max": 100, "min": 0}]


radar = Radar("")
radar.config(c_schema=c_schema,radar_text_size=20)
radar.add("同类基金", value2, item_color='#9C9C9C',legend_orient='vertical',legend_pos='65%',
         legend_text_size=20,symbol=None,
         area_color= '#9C9C9C', area_opacity=0.3,
          is_legend_show=False)
radar.add("交银成长混合A", value1, item_color=' #074541',legend_orient='vertical',legend_pos='65%',
         legend_text_size=20,
         area_color= ' #074541', area_opacity=0.8,
          is_legend_show=False,line_width=3)

date2 = ['第一大行业','前三大行业','前五大行业']
tz_1 =[41.57,60.42,72.26]
tz_2 =[32.55,48.47,53.78]
bar2 = Bar("行业投资集中度",subtitle='单位：%',width=400)
bar2.add('交银成长混合A',date2,tz_1,yaxis_min=0,yaxis_max=80,legend_top='5%')
bar2.add('同类平均',date2,tz_2,yaxis_min=0,yaxis_max=80,legend_top='5%')

date3 = ['该基金','公司同类平均','全行同类平均']
gp_1 =[72.04,70.75,63.83]
bar3 = Bar("前十大股票投资集中度",subtitle='单位：%',width=400)
bar3.add('',date3,gp_1,yaxis_min=50,yaxis_max=80,bar_category_gap=60,legend_top='5%',label_color=['#F7887F'])

heatx_axis = ["价值", "平衡", "成长"]
heaty_axis = ["大盘", "中盘", "小盘"]
data = [[0,0,1],[0,1,1],[0,2,1],
        [1,0,1],[1,1,1],[1,2,39],
        [2,0,1],[2,1,0],[2,2,55]]


heatmap = HeatMap('基金股票投资风格箱',subtitle='2：大盘\n1：中盘\n0：小盘',width=400,height=400)
heatmap.add(
    "",
    heatx_axis,
    heaty_axis,
    data,
    is_visualmap=True,
    visual_range=[0,55],
    visual_range_color=[ '#ffffff', '#7E70AC'],
    visual_text_color="#000",
    visual_orient="horizontal"
)

page = Page()
page.add(barcy)
page.add(line)
page.add(bar1)
page.add(pie1)
page.add(bar2)
page.add(bar3)
page.add(radar)
page.add(heatmap)
page.render(path='C:/Users/Administrator/Desktop/fund1.html')