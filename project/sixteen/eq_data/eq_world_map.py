from pathlib import Path
import plotly.express as px
import json
import pandas as pd

#将数据作为字符串读取并转换为python对象
#path =Path('eq_data/eq_data_1_day_m1.geojson')

path =Path('eq_data/eq_data_30_day_m1.geojson')

try:
    contents=path.read_text()
except:
    contents=path.read_text(encoding='utf-8')

#以字符串数据类型读取文件，
#contents=path.read_text()

#字符串转换python对象
all_eq_data=json.loads(contents)

#将数据文件转换为更易读的版本
path=Path('eq_data/readable_eq_data.gojson')


#json.dumps()用来存储，指定数据结构中嵌套元素的缩进量
readable_contents=json.dumps(all_eq_data,indent=4)

#将可读内容写入文件
path.write_text(readable_contents)

#地震列表创建
#提取和键'features'相关联数据
all_eq_dicts=all_eq_data['features']
print(len(all_eq_dicts))


#提取位置数据

mags,titles,lons,lats=[],[],[],[]
for eq_dict in all_eq_dicts:
    #获取震级
    mag=eq_dict['properties']['mag']
    title=eq_dict['properties']['title']
    
    #获取地震的位置数据（经纬度）
    lon=eq_dict['geometry']['coordinates'][0]
    lat=eq_dict['geometry']['coordinates'][1]
    
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

'''
fig=px.scatter(
    x=lons,
    y=lats,
    labels={'x':'经度','y':'纬度'},
    
    #设置散点图可以表示的经纬度的范围
    range_x=[-200,200],
    range_y=[-90,90],
    
    #设置散点图的像素
    width=800,
    height=800,
    title='全球地震散点图'
)
'''  

#封装数据
data=pd.DataFrame(
    data=zip(lons,lats,titles,mags, ),columns=['经度','纬度','位置','震级'])

data.head()

#配置参数
fig=px.scatter(
    data,
    x='经度',
    y='纬度',
    
    
    #设置散点图可以表示的经纬度的范围
    range_x=[-200,200],
    range_y=[-90,90],
    
    #设置散点图的像素
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    #震级字段像素
    
    #不同标记颜色表示震级，数值越小越蓝，数值越大越黄
    color='震级',
    
    #添加悬停文本
    hover_name='位置'
)

fig.write_html('global_earthquakes.html')
fig.show()