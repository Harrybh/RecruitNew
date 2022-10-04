import requests
import re
import xlwt
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'
}
# 模拟电脑登录
Work_Book = xlwt.Workbook(encoding = "utf-8")
Work_Sheet = Work_Book.add_sheet("TIOBE")
Work_Sheet.col(0).width = 15 * 256
Work_Sheet.col(1).width = 15 * 256
Work_Sheet.col(2).width = 15 * 256
# 创建
# Work_Book.save("Tiobe_Data.xls")
style = xlwt.XFStyle()
font = xlwt.Font()
font.height = 20*16
font.name = "Times New Roman"
font.bold = True
border = xlwt.Borders()
border.left = xlwt.Borders.THIN
border.right = xlwt.Borders.THIN
border.top = xlwt.Borders.THIN
border.bottom = xlwt.Borders.THIN
alignment = xlwt.Alignment()
alignment.horz = 0x02
alignment.vert = 0x01
style.borders = border
style.font = font
style.alignment = alignment
# 单元格样式设定
Work_Sheet.write_merge(0, 0, 0, 2, "TIOBE 编程语言排行榜数据汇总", style)
Work_Sheet.write(1, 0, "Name", style)
Work_Sheet.write(1, 1, "Date", style)
Work_Sheet.write(1, 2, "Heat", style)
Rep = requests.get('https://www.tiobe.com/tiobe-index/', headers=headers).text
Data = re.findall('{name : (.*?),data : (.*?)}', Rep)
#
x = ['0'] * 22
Year_Num = 2001
while Year_Num <= 2022:
    x[Year_Num-2001] = str(Year_Num) + "年"
    Year_Num += 1
line = Line(init_opts=opts.InitOpts(width="2000px",height="800px"))
line.add_xaxis(xaxis_data=x)
line.set_global_opts(title_opts=opts.TitleOpts(title="TIOBE"))
#
Name = [eval(i[0]) for i in Data]
Dates = [j[1] for j in Data]
Line_Num = 2
for x in range(len(Dates)):
    name = Name[x]
    datas = re.findall(r'\[Date.UTC(.*?)\]', Dates[x], re.DOTALL)
    # print(name)
    Year = 2001
    cnt = 0;
    Now_sum = 0;
    y = [0] * 22
    # print("finish")
    for m in datas:
        # print(Line_Num)
        data1 = re.findall(r'\d+', m)
        data2 = data1[0] + '.' + data1[1] + '.' + data1[2]
        data3 = data1[3] + '.' + data1[4]
        Work_Sheet.write(Line_Num, 0, name, style)
        Work_Sheet.write(Line_Num, 1, data2, style)
        Work_Sheet.write(Line_Num, 2, data3, style)
        Line_Num += 1
        # print(int(data1[0]))
        while Year != int(data1[0]):
            if cnt:
                y[Year - 2001] = round(Now_sum / cnt, 1)
            else:
                y[Year - 2001] = 0
            Now_sum = 0
            cnt = 0
            Year += 1
        Now_sum += float(data3)
        cnt += 1
        # print(data2,data3)
    line.add_yaxis(series_name=name, y_axis=y, is_connect_nones=True)

Work_Book.save("Tiobe_Data.xls")
line.render_notebook()
make_snapshot(snapshot, line.render(), "data.png")


