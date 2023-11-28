from pathlib import Path
from datetime import datetime 
import csv
import matplotlib.pyplot as plt 


#sitka_weather_07-2021_simple文件数据绘制折线图

#创建Path对象，指向数据文件
#path=Path('weather_data/sitka_weather_07-2021_simple.csv')

#sitka_weather_2021_simple文件数据绘制折线图
path=Path('weather_data/sitka_weather_2021_simple.csv')

#将获取的文件中各行以列表数据类型赋值给lines
lines=path.read_text().splitlines()

#创建reader对象，解释文件各行
reader=csv.reader(lines)

#调用next()函数得到第一行的内容
header_row=next(reader)
#print(header_row)

#调用enumerate()函数获取每个元素的索引及其值
'''
for index ,column_header in enumerate(header_row):
    print(index,column_header)
'''

    


#提取最高温度
'''
#创建名为highs的空列表，用来放最高温度
highs=[]

#遍历文件中的各行，从之前中断的地方开始遍历
for row in reader:
    #前面通过enumerate()函数已经知道最高温度所在列
    high=int(row[4])
    highs.append(high)

#print(highs)

'''


'''
#根据最高温度绘图，数据点颜色为红色


plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(highs,color='red')

#设置绘图的格式

#sitka_weather_07-2021_simple文件折线图 设置标题
#ax.set_title("Daily High Temperatures, July 2021",fontsize=24)

#设置Y坐标字号
ax.set_ylabel('',fontsize=16)

#设置图表中刻度标签的字号
ax.tick_params(labelsize=16)

#plt.show()

'''


#将字符串类型的日期转换为指定格式日期


#创建一个标识2021年7月1日的对象
#第一个参数是实参，包含日期的字符串，第二个参数是需要设置日期的格式
first_date=datetime.strptime('2021-07-01','%Y-%m-%d')

#print(first_date)


#提取日期和最高温度，并绘制图

dates,highs=[],[]

for row in reader:
    current_date=datetime.strptime(row[2],'%Y-%m-%d')
    high=int(row[4])
    highs.append(high)
    dates.append(current_date)

plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates,highs,color='red')

#设置绘图的格式

#设置标题
ax.set_title("Daily High Temperatures, 2021",fontsize=24)

#设置x坐标字号
ax.set_xlabel('',fontsize=16)

#调用函数绘制倾斜的日期标签
fig.autofmt_xdate()

#设置x坐标名称，字号
ax.set_ylabel("Temperature(F)",fontsize=16)
#设置图表中刻度标签的字号
ax.tick_params(labelsize=16)

plt.show()