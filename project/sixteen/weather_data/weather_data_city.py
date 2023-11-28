from pathlib import Path
from datetime import datetime 
import csv
import matplotlib.pyplot as plt 

#sitka_weather_2021_simple文件数据绘制折线图
path=Path('sixteen/weather_data/beijing_data.csv')

#将获取的文件中各行以列表数据类型赋值给lines
lines=path.read_text().splitlines()

#创建reader对象，解释文件各行
reader=csv.reader(lines)

#调用next()函数得到第一行的内容
header_row=next(reader)

#创建一个标识2021年7月1日的对象
#第一个参数是实参，包含日期的字符串，第二个参数是需要设置日期的格式
first_date=datetime.strptime('2021-07-01','%Y-%m-%d')



#提取日期,最高温度和最低温度，并绘制图

dates,highs,lows=[],[],[]

#获取日期，最高温度，最低温度
for row in reader:
    current_date=datetime.strptime(row[0],'%Y-%m-%d')
    high=int(row[2])
    highs.append(high)
    low=int(row[3])
    lows.append(low)
    dates.append(current_date)

plt.style.use('seaborn')
fig,ax=plt.subplots()

#日期和最高温度确定的数据点颜色为红色
#ax.plot(dates,highs,color='red')

#日期和最低温度确定的数据点颜色为蓝色
#ax.plot(dates,lows,color='blue')

#设置日期和最高温度确定的数据点颜色为红色，透明度为0.5
ax.plot(dates,highs,color='red',alpha=0.5)

#设置日期和最低温度确定的数据点颜色为蓝色，透明度为0.5
ax.plot(dates,lows,color='blue',alpha=0.5)

#最高温度和最低温度之间区域设置背景为蓝色，透明度为0.1
ax.fill_between(dates,lows,highs,facecolor='blue',alpha=0.1)

#设置绘图的格式

#设置标题
ax.set_title("Beijing Daily High and Low Temperatures, 2023-10-01-2023-11-15",fontsize=18)

#设置x坐标字号
ax.set_xlabel('',fontsize=16)

#调用函数绘制倾斜的日期标签
fig.autofmt_xdate()

#设置x坐标名称，字号
ax.set_ylabel("Temperature(F)",fontsize=16)
#设置图表中刻度标签的字号
ax.tick_params(labelsize=16)

plt.show()