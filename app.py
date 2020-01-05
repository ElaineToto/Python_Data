import random
from calendar import c
from tkinter import Grid

from flask import Flask,render_template,request
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map, EffectScatter, HeatMap, Line,Grid
from pyecharts.faker import Faker
from pyecharts.globals import SymbolType
from pyecharts.charts import Pie,Bar

df = pd.read_csv('data1.csv')
app = Flask(__name__)


@app.route('/')
def map() -> 'html':
    a = (
        Map()
            .add("平均月薪", list(zip(df.省, df.平均月薪)), "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="各省python相关岗位平均月薪"),
            visualmap_opts=opts.VisualMapOpts(min_=7164.08, max_=17096.07),
        )
    )
    a.render("./templates/map.html")
    with open("./templates/map.html", encoding="utf8", mode="r") as f:
        map = "".join(f.readlines())
        the_select_province = {'北京':'4924',
                               '上海':'3114',
                               '广东':'3164',
                               '浙江':'1244',
                               '南京':'701',
                               '湖北':'412',
                               '江苏':'450',
                               '福建':'359',
                               '四川':'985',
                               '辽宁':'227',
                               '安徽':'236',
                               '湖南':'239',
                               '山东':'360',
                               '吉林':'88',
                               '江西':'60',
                               '天津':'355',
                               '山西':'417',
                               '陕西':'60',
                               '重庆':'179',
                               '黑龙江':'60',
                               '河南':'477',
                               '贵州':'60',
                               '河北':'60',}

    return render_template('python_map.html',
                           the_map=map,
                           the_province=the_select_province
                           )






@app.route('/effectscatter_symbol')
def effectscattere_symbol() -> 'html':
    df = pd.read_csv('data2.csv',encoding = 'utf8', index_col="名称")
    省 = list(df.loc["省"].values)[-24:]
    数量 = list(df.loc["数量"].values)[-24:]
    value = [[i, j, random.randint(0, 80)] for i in range(24) for j in range(24)]
    c = (
        HeatMap()
            .add_xaxis(省)
            .add_yaxis("数量", 数量, value)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="各省Python相关岗位数量"),
            visualmap_opts=opts.VisualMapOpts(),
        )
    )
    c.render("./templates/effectscatter_symbol.html")
    with open("./templates/effectscatter_symbol.html", encoding="utf8", mode="r") as f:
        sym = "".join(f.readlines())
        return render_template('python_effectscatter_symbol.html',
                               the_sym=sym,
                               )

        1



@app.route('/pie_base')
def pie_base() -> 'html':
    df = pd.read_csv('data3.csv', encoding='utf8')
    bar = (
        Bar()
            .add_xaxis(['不限', '3-5年', '1-3年', '5-10年', '无经验', '一年以下', '10年以上'])
            .add_yaxis("职位数量", [6183, 5164, 4842, 1516, 366, 111, 34])

            .set_global_opts(title_opts=opts.TitleOpts(title="工作经验-职位分布数量"))
    )

    line = (
        Line()
            .add_xaxis(['本科', '大专', '不限', '硕士', '博士', '中专'])
            .add_yaxis("职位数量", [9954, 3704, 3205, 1137, 88, 31])

            .set_global_opts(
            title_opts=opts.TitleOpts(title="最低要求学历-职位分布数量", pos_top="50%"),
            legend_opts=opts.LegendOpts(pos_top="50%"),
        )
    )

    grid = (
        Grid()
            .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%", pos_right="0", height="30%"))
            .add(line, grid_opts=opts.GridOpts(pos_top="60%", pos_right="0", height="30%"))
    )
    bar,line,grid.render("./templates/pie_base.html")
    with open("./templates/pie_base.html", encoding="utf8", mode="r") as f:
        pie_base = "".join(f.readlines())
        return render_template('python_pie_base.html',
                               the_pie_base=pie_base,
                               )



@app.route('/Bar/')
def bar_base() -> Bar:
    df = pd.read_csv('data4.csv', encoding='utf8', index_col="学历")
    最低学历 = list(df.loc["最低学历"].values)[-6:]
    无经验 = list(df.loc["无经验"].values)[-6:]
    一年以下 = list(df.loc["一年以下"].values)[-6:]
    不限 = list(df.loc["不限"].values)[-24:]
    一至三年 = list(df.loc["一至三年"].values)[-24:]
    三至五年 = list(df.loc["三至五年"].values)[-24:]
    五至十年 = list(df.loc["五至十年"].values)[-24:]
    十年以上 = list(df.loc["十年以上"].values)[-24:]
    c = (
        Line()
            .add_xaxis(最低学历)

            .add_yaxis("无经验", 无经验)
            .add_yaxis("一年以下", 一年以下)
            .add_yaxis("不限", 不限)
            .add_yaxis("一至三年", 一至三年)
            .add_yaxis("三至五年", 三至五年)
            .add_yaxis("五至十年", 五至十年)
            .add_yaxis("十年以上", 十年以上)
            .set_global_opts(title_opts=opts.TitleOpts(title="最低学历-工作经验与平均月薪",
                                                       subtitle="平均月薪(元)"))
    )
    c.render("./templates/Bar.html")
    with open("./templates/Bar.html", encoding="utf8", mode="r") as f:
        bar_base= "".join(f.readlines())
        return render_template('python_bar.html',
                               the_bar_base=bar_base,
                               )


if __name__ == '__main__':
    app.run(debug=True)
