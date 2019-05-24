from pyecharts import Kline
from pyecharts import EffectScatter
from pyecharts import Line
from pyecharts import Bar
from pyecharts import Overlap
import tushare as ts
import pandas as pd
import stockstats
from pyecharts import Page

pro = ts.pro_api()

def backtesting_plot(table_name, indicator_name_list,vol_name_list,stockStat):
    # data preparation
    da = pd.DataFrame(data=table_name)
    da['vol'] = da['vol'].apply(lambda vol: vol if vol > 0 else 0)
    date = da["trade_date"].apply(lambda x: str(x)).tolist()
    k_plot_value = da.apply(lambda record: [record['open'], record['close'], record['low'], record['high']],
                            axis=1).tolist()

    # K chart
    kline = Kline()
    kline.add("SZZZ", date, k_plot_value,
              mark_point=["max"],
              is_datazoom_show=True)

    indicator_lines = Line()
    for indicator_name in indicator_name_list:
        indicator_lines.add(indicator_name, date, da[indicator_name].tolist())
    # trading volume bar chart
    bar = Bar()
    bar.add("vol", date, da["vol"],
            tooltip_tragger="axis", is_legend_show=False, is_yaxis_show=False, yaxis_max=5 * max(da["vol"]))
    # buy and sell
    es = EffectScatter("buy")
    stockStat['rsi_10'].tolist()
    print(df2[df2.rsi_10 > 79.5])
    rsi10_selllist = df2[df2.rsi_10 > 75]
    rsi10_buylist = df2[df2.rsi_10 < 25]
    es.add("sell", x_axis=rsi10_selllist['trade_date'], y_axis=rsi10_selllist['high'], symbol_size=5)
    es.add("buy", x_axis=rsi10_buylist['trade_date'], y_axis=rsi10_buylist['open'], symbol_size=5,symbol='arrow')

    vol_line = Line()
    for vol_name in vol_name_list:
        vol_line.add(vol_name, date, da[vol_name].tolist())

    rsi_line = Line()
    for rsi_name in ['rsi_5', 'rsi_10']:
        rsi_line.add(rsi_name, date, stockStat[rsi_name].tolist(),
                     is_datazoom_show=True,datazoom_type="both")



    overlap = Overlap()
    overlap.add(kline,yaxis_index=0)
    overlap.add(es, yaxis_index=0)
    overlap.add(indicator_lines,yaxis_index=0)
    overlap.add(bar, yaxis_index=1, is_add_yaxis=True)
    overlap.add(vol_line, yaxis_index=1, is_add_yaxis=True)

    page = Page()
    page.add(overlap)
    # page.add(rsi_line)
    page.render(path='C:/Users/Administrator/Desktop/tt.html')



df1 =ts.pro_bar(pro_api=pro, ts_code='601577.SH', start_date='20180101', end_date='20190414', ma=[5, 10, 30, 60])
df2 =  df1.sort_values(by="trade_date",ascending = True)
stockStat = stockstats.StockDataFrame.retype(df2)
indicator_name_list =['ma5','ma10','ma30','ma60']
vol_name_list =['ma_v_5','ma_v_10','ma_v_30','ma_v_60']
backtesting_plot(df2,indicator_name_list,vol_name_list,stockStat )

