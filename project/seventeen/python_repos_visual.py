import requests
import plotly.express as px 

#执行API调用并查看响应
url="https://api.github.com/search/repositories"
url += "?q=language:python_sort:stars+stars:>10000"

headers={"Accept":"application/vnd.github.v3+json"}

#响应请求是否成功
r=requests.get(url,headers=headers)
print(f"Status code:{r.status_code}")

#将响应转换为字典
response_dict=r.json()

#处理结果
#print(response_dict.keys)

#所有符合条件的仓库数目
#print(f"Total_repositories:{response_dict['total_count']}")
#检测API返回的结果是否完整
print(f"Complete results : {not response_dict['incomplete_results']}")

#处理有关仓库的信息
repo_dicts=response_dict['items']

#repo_names,stars,hover_texts =[],[],[]

repo_links,stars,hover_texts=[],[],[]

#获取仓库项目名称，所获得的星数
for repo_dict in repo_dicts:
    
    #repo_names.append(repo_dict['name'])
    
    #将仓库名转换为链接
    repo_name=repo_dict['name']
    repo_url=repo_dict['html_url']
    repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    #创建悬停文本
    owner=repo_dict['owner']['login']
    description=repo_dict['description']
    hover_text=f"{owner}<br />{description}"
    hover_texts.append(hover_text)

#可视化图，确定标题，x轴，y轴 
title="Most-Starred Python Projects on Github"
labels={'x':'Repository','y':'Stars'}

#项目名称，星数，所有者和描述
#fig=px.bar(x=repo_names,y=stars,title=title,labels=labels,hover_name=hover_texts)

#链接形式的可视化图设置
fig=px.bar(x=repo_links,y=stars,title=title,labels=labels,hover_name=hover_texts)

#设置标题，x轴，y轴字号大小
fig.update_layout(title_font_size=28,xaxis_title_font_size=20,yaxis_title_font_size=20)

#定制标记颜色
fig.update_traces(marker_color='SteelBlue',marker_opacity=0.6)
fig.show()