from pathlib import Path
import json

#将数据作为字符串读取并转换为python对象
path =Path('eq_data/eq_data_1_day_m1.geojson')

#以字符串数据类型读取文件，
contents=path.read_text()

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

#提取震级
'''
mags=[]
for eq_dict in all_eq_dicts:
    #获取字典的'properties'部分的'mag'键下的值
    mag=eq_dict['properties']['mag']
    mags.append(mag)

print(mags[:10])
'''

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

#print(mags[:10])
#print(titles[:2])
#print(lons[:5])
#print(lats[:5])


