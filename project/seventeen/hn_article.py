import requests
import json
from operator import itemgetter

#执行API调用并存储响应
url="http://hacker-news.firebaseio.com/v0/topstories.json"
r=requests.get(url)
print(f"Status code : {r.status_code}")

#探索数据结构
'''
response_dict=r.json()
response_string=json.dumps(response_dict,indent=4)
print(response_string)
'''

submission_ids=r.json()
submission_dicts=[]


for submission_id in submission_ids[:5]:
    #对于每篇文章，都执行一个API调用
    url=f"http://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r=requests.get(url)
    print(f"id:{submission_id}\status:{r.status_code}")
    response_dict=r.json()
    
    
#对于每篇文章，都创建一个字典，存储文章的标题，链接和评论
    submission_dict={
        'title':response_dict['title'],
        'hn_link':f"https://news.ycombinator.com/item?id={submission_id}",
        'comments':response_dict['descendants'],
    }

    submission_dicts.append(submission_dict)

#根据评论数对文章进行排序
submission_dicts=sorted(submission_dicts,key=itemgetter('comments'),reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle:{submission_dict['title']}")
    print(f"\nDiscussion Link:{submission_dict['hn_link']}")
    print(f"\nComments:{submission_dict['comments']}")