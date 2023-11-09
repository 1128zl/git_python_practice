#喜欢的书

'''
def favorite_book(title):
    print(f"One of my favorite books is {title}.\n")
    
favorite_book('the king')
'''
#城市 
'''
country='China'
cities=['beijing','shanghai','shenzhen']
def describe_country(country,city):
    if city.lower() in cities : 
        print(f"{city.title()} is in {country.title()}.\n")
    

describe_country(country,'shanghai')
describe_country(country,'Beijing')
describe_country(country,'shouer')
'''

#专辑

'''
def make_album(s_name,c_name,count=''):
    albums={}
    albums['singer']=s_name
    albums['cd']=c_name
    
    if(count!=''):
        albums['number']=count
    return albums

'''

#print(make_album('邓紫棋','启示录'))
#print(make_album('易烊千玺','刘艳芬',8))
#print(make_album('王源','客厅狂欢'))
'''


def user_create():
    for i in range(3):
        print("\nPlease input two messages:\n")
        s_name=input("signer name :")
        c_name=input("\ncd name :")
        print(make_album(s_name,c_name))
        
        
user_create()
'''

#消息

'''
messages=['how are you?','I am fine.','Good night!']
def show_messages():
    for message in messages:
        print(message)

send_messages=[]       
def send_messages_fun():
    for message in messages:
        send_messages.append(message)
        
show_messages()
send_messages_fun()
for message in send_messages:
        print(message)
'''
#汽车
'''
def make_car(manuf,type,**car_info):
    car_info['制造商']=manuf
    car_info['型号']=type
    return car_info
print(make_car('比亚迪','型号1',color='green',value='200000'))
'''
'''
from six_practice_2 import *
print("What do you think of today?\n")
describe()
'''
'''
import six_practice_2
six_practice_2.describe()
'''

from six_practice_2 import describe
print("What do you think of today?\n")
describe()