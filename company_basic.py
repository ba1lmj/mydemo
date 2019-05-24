import pyecharts
import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Administrator/Desktop/txpj.csv',encoding='gb2312')
print(df)
df1 = df[['basic','stability','invest']]
data = np.array(df1)
data_list = data.tolist()
print(data)
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
    '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
# def label_formatter(params):
#     return params.seriesName +'分'

def label_formatter(params):
    return params.ser +'分'
scatter3D = Scatter3D("3D 散点图示例", width=800)
for i in range(0,87):
    scatter3D.add(df.iat[i,0], [data[i],[0,0,0]] , is_legend_show=False,
                  visual_split_number=5,is_visualmap=True,visual_dimension=2,visual_range_color=range_color,
                xaxis3d_name='Basic strength score',yaxis3d_name='Stability score',zaxis3d_name='The ability to\n manage investments',
                label_formatter='{a}',xaxis3d_rotate=90,yaxis3d_rotate=90,zaxis3d_rotate=90,)

scatter3D.render('C:/Users/admin/Desktop/可视化代码/company_basic.html')

