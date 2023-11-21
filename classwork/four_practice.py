# 6.3

'''
like_number={'name_1':'jack','name_2':'helen','name_3':'lily'}
for key,value in like_number.items():
    print(f"\nname:{key}")
    print(f"\nlikenum:{value}")
'''

#6.4

'''
country_river={'nile':'egypt','yangtze':'china','hudson':'america'}
for key,value in country_river.items():
    print(f"\n{'The'} {key} {'runs through'} {value}.")
    print(f"\n{'河流：'} {key}")
    print(f"\n{'国家：'} {value}")
'''

#6.7
'''
like_number1={'name_1':'jack','name_2':'helen','name_3':'lily'}
like_number2={'name_4':'zhangsan','name_5':'wangwu','name_6':'lisi'}
like_number3={'name_7':'lihua','name_8':'liuyan','name_9':'xiehui'}
peoples=[like_number1,like_number2,like_number3]
for people in peoples :
    print(people)
'''
#6.11
'''
cities={'china':{'country':'china','population':'17 billion','fact':'A big country'},
        'korea':{'country':'korea','population':'0.5 billion','fact':'A small country'},
        'japan':{'country':'japan','population':'severals million','fact':'A foolish country'}}
for country_name,mesg in cities.items():
    print(f"\ncountry_name:{country_name}")
    print(f"\ncountry={mesg['country']}")
    print(f"\npopulation={mesg['population']}")
    print(f"\nfact={mesg['fact']}")
'''

#7.2

'''
number=input("How many people will come to have lunch?\n")  
if(int(number)>8):
    print("There is not have empty seats.\n")
else :
    print("There is have empty seats.\n")
'''

#7.5
#第一种方式
'''
material=input("Which kind of material you want to add?\n")
while(material!='quit'):
    print(f"I want to add {material}.\n")
    material=input("Which kind of material you want to add?\n")
print("There will not have material to add.\n")
'''

#第二种方式  
'''
active=True
while(active):
    material=input("Which kind of material you want to add?\n") 
    if(material=='quit'):
        active=False
    else :
         print(f"I want to add {material}.\n")
    
print("There will not have material to add.\n")
'''

#第三种方式
'''
material=input("Which kind of material you want to add?\n")
while(True):
    if(material=='quit'):
        break
    else:
        print(f"I want to add {material}.\n")
        material=input("Which kind of material you want to add?\n")
print("There will not have material to add.\n")
'''

#7.9
'''
sandwich_orders=['tunna sandwich','pastrami sandwich','fruit sandwich']
sandwich_orders.insert(0,'pastrami sandwich')
sandwich_orders.append('pastrami sandwich')

print("It is not have pastrami sandwiches . ")

finished_sandwiches=[]
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')


print("\nsandwich_orders:")  
for sandwich in sandwich_orders:
    print(sandwich)
    finished_sandwiches.append(sandwich)
    
print("\nfinished_sandwiches:")  
for sandwich in finished_sandwiches:
    print(sandwich)
print('pastrami sandwich' not in finished_sandwiches)
'''



