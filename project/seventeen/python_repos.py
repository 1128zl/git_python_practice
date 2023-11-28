import requests

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
print(f"Total_repositories:{response_dict['total_count']}")
#检测API返回的结果是否完整
print(f"Complete results : {not response_dict['incomplete_results']}")

#探索有关仓库信息
#返回的所有仓库的详细信息列表
repo_dicts=response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

#研究第一个仓库
repo_dict=repo_dicts[0]
#仓库详细信息字典中所有的键的数量
#print(f"\nKeys: {len(repo_dicts)}")

#排序键打印键
'''
for key in sorted(repo_dict.keys()):
    print(key)
'''

print("\nSelected information about first repository:")

#打印项目名称
print(f"Name:{repo_dict['name']}")

#所有者的登录名
print(f"Owner:{repo_dict['owner']['login']}")

#项目所获得的的星数
print(f"Stars:{repo_dict['stargazers_count']}")

#仓库URL
print(f"Repository:{repo_dict['html_url']}")

#仓库创建时间和最后一次更新时间
print(f"Created:{repo_dict['created_at']}")
print(f"Updated:{repo_dict['updated_at']}")
print(f"Description:{repo_dict['description']}")