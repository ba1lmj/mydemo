from pyecharts.charts import Boxplot,Radar,HeatMap,Page
import numpy as np
import pandas as pd

value1 = [[70,55,25,50,55,35]]
#用于调整雷达各维度的范围大小
c_schema= [{"name": "平均收益率评分", "max": 100, "min": 0},
           {"name": "超额收益率评分", "max": 100, "min": 0},
           {"name": "稳定能力评分", "max": 100, "min": 0},
           {"name": "择时能力评分", "max": 100, "min": 0},
           {"name": "选股能力评分", "max": 100, "min": 0}]


radar = Radar("公司基金经理各项能力评分")
radar.config(c_schema=c_schema,radar_text_size=20)
radar.add("王少成", value1, item_color='#0A5E59',legend_orient='vertical',legend_pos='65%',
         legend_text_size=20,
          symbol=None,area_color= '#0A5E59', area_opacity=0.5,
          is_legend_show=False,line_width=3)

heatx_axis = ["价值", "平衡", "成长"]
heaty_axis = ["大盘", "中盘", "小盘"]
data = [[0,0,0],[0,1,0],[0,2,6.69],
        [1,0,0],[1,1,0],[1,2,45.55],
        [2,0,0],[2,1,0.325],[2,2,44.95]]

heatmap = HeatMap('基金经理股票投资风格箱',subtitle='2：大盘\n1：中盘\n0:小盘',width=400,height=400)
heatmap.add(
    "",
    heatx_axis,
    heaty_axis,
    data,
    is_visualmap=True,
    visual_range=[0,50],
    visual_range_color=[ '#ffffff', '#6699CC','#486189'],
    visual_text_color="#000",
    visual_orient="horizontal",
)

page = Page()
page.add(radar)
page.add(heatmap)
page.render(path='C:/Users/Administrator/Desktop/people.html')