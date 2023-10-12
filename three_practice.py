# 3.1
'''
names =['helen','jack','rose','jackson']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names)
'''


# 3.2
'''
mesg="how are you"
print(f"{names[0].title()},{mesg} ?")
print(f"{names[1].title()},{mesg} ?")
print(f"{names[2].title()},{mesg} ?")
print(f"{names[3].title()},{mesg} ?")
'''
# 3.3
'''
ways = ["bicycle","motorcycle","bus"]
particulars =['i would like to take a','is a good way for the earth','maybe meet accidents']
print(f"{ways[0].title()} {particulars[1]}.")
print(f"{ways[1].title()} {particulars[2]}.")
print(f"{particulars[0].title()} {ways[2]} .")
'''
# 3.4
'''
persons =['易烊千玺','康康','卢洋洋']
mesg1 ="今天有时间一起吃饭吗"
mesg2 ="有事不能赴约"
# print("初步邀请嘉宾名单：")
print(f"\n{persons[0]},{mesg1} ?")
print(f"{persons[1]},{mesg1} ?")
print(f"{persons[2]},{mesg1} ?")

# 3.9 清点晚餐嘉宾
print(len(persons))
'''


# 3.5
''''
print(f"\n{persons[2]}{mesg2}。")
persons[2]='周雨彤'

# print("\n最终邀请嘉宾名单：")
print(f"\n{persons[0]},{mesg1} ?")
print(f"{persons[1]},{mesg1} ?")
print(f"{persons[2]},{mesg1} ?")
'''


# 3.6
'''
persons.insert(0,'沈月')
persons.insert(2,'王敬轩')
persons.append("林允")

# print(persons)

print(f"\n{persons[0]},{mesg1} ?")
print(f"{persons[1]},{mesg1} ?")
print(f"{persons[2]},{mesg1} ?")
print(f"{persons[3]},{mesg1} ?")
print(f"{persons[4]},{mesg1} ?")
print(f"{persons[5]},{mesg1} ?")
'''



# 3.7
'''
print("\n由于食材原因，目前只能邀请两位嘉宾。")


while(len(persons)>2):
    
    people=persons.pop()
    print(f"{people},{'很抱歉本次无法邀请您来共进晚餐'}。")

print(persons)

print(f"\n{persons[0]},{'您依然在受邀之列'}。")
print(f"{persons[1]},{'您依然在受邀之列'}。")

del persons[0]
del persons[0]

print(persons)
'''

# 3.8
'''
places =['shanghai','beijing','suzhou','chongqing','xian']

print(places)
print()

#  sorted() 字母顺序打印
print(sorted(places))
print()

#sorted() 字母顺序反向打印 
print(sorted(places,reverse=True))
print()

#检查是否places本身的顺序被改变
print(places)
print()

# reverse()修改places顺序
places.reverse()

print(places)
print()

places.reverse()

# reverse() 将places顺序改回来
print(places)
print()

'''

#sort() 字母顺序

'''
# print(places.sort())
# 因为places.sort(reverse=True)和places.sort()没有返回值，所以打印的就是None
places.sort()
print()

# 检查sort()方法可不可以对本身顺序造成不可逆的改变
print(places)
print()

# sorted() 字母顺序反向打印
# print(places.sort(reverse=True))
places.sort(reverse=True)

print(places)

'''
# 3.10
#things =['wugongshan','ocean','park','ice cream','live house']

#列表的打印顺序方面
# sort()函数
#things.sort()
#things.sort(reverse=True)

#sorted() 函数
#print(sorted(things))
#print(sorted(things,reverse=True))

#增删改查

#things[0]='snow'
#del things[2]
#things.insert(0,'plain')
#things.pop(2)
#things.remove('park')
#things.append('bridge')
#print(things)

#3.11
# print(things[5])

#4.2
'''
animals=['panda','dog','cat','horse']
for animal in animals :
    print(animal)
    print(f"{'A'} {animal} {'would make a great pet'}.")
print(f"{'Any of these animals would make a great per'}!")
'''
# 4.3
'''
for value in range(1,21):
    print(value)
'''
# 4.4

'''
values =list(range(1,1000001))
# print(values)
print(min(values),max(values),sum(values))
'''
# 4.6
'''
list_1=[(value-1)*2+1 for value in range(1,11)]
print(list_1)
'''

# 4.7
'''
list_2=[(value)*3 for value in range(1,10)]
print(list_2)
'''

# 4.8  4.9
'''

'''
# list_3=[value**3 for value in range(1,11)]
#for value in list_3:
    # print(value)
    
# 4.10
'''
print('The first three items in the list are:')
print(list_3[0:3])
print(list_3[:3])

print('The items from the middle of the list are:')
print(list_3[3:6])

print('The last three items in the list are:')
print(list_3[-3:])
print(list_3[7:])
'''

#4.11
'''
pizzas=['pizza_1','pizza_2','pizza_3']
friend_pizzas=pizzas[:]
pizzas.append('pizza_6')
friend_pizzas.append('pizza_9')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
    
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
    
'''

# 4.13
'''
foods=('noodles','cake','rice','apple')
for food in foods:
    print(food)
# foods[1]='ice cream'

foods=('ice cream','cake','orange','apple')
for food in foods:
    print(food)
'''


# 5.1

'''
car ='subaru'
print("Is car == 'subaru'? I predict True.")
print(car  == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car  == 'audi')

print(car=='subaru')
print(car=='bus')
print(car=='subaru')
print(car=='motor')
print(car=='airplane')
print(car=='subaru')
'''

# 5.2
'''
m='CAR'
print('subaru'=='car')
print()

print('subaru'=='subaru')
print()

print(m.lower()=='subaru')
print()

print(m.lower()=='car')
print()

print(5 in range(1,5) and 5%2)

print(5 in range(1,5) or 4 in range(1,5))
'''

# 5.3  5.4  5.5
'''
alien_color='yellow'
if(alien_color=='green'):
    print("You win 5 scores!")
elif(alien_color=='red'):
    print("You win 10 scores!")
else :
    print("You win 15 scores!")
'''

# 5.6
'''
age =15
if(age<2):
    print("The person is a baby.")
elif(age<4):
    print("The person is a child.")
elif(age<13):
    print("The person is a children.")
elif(age<18):
    print("The person is a juvenile.")
elif(age<65):
    print("The person is a young and middle age adult.")
else:
    print("The person is a old man.")
'''

# 5.7
'''
fruit_list=['banana','apple','orange','grape','watermelon']
for fruit in fruit_list:
    if fruit =='orange':
        print("You really like orange.")
    if fruit =='apple':
        print("You really like apple.")
    if fruit =='peach':
        print("You really like peach.")
    if fruit =='cherry':
        print("You really like cherry.")
    if fruit =='watermelon':
        print("You really like watermelon.")
'''

# 5.8 5.9
'''
users_name=['jack','helen','lily','admin']

for name in users_name:
    if(name=='admin'):
        print("Hello admin,would you like to see a status report?")
    else:
        print(f"{'Hello'} {name.title()},{'thank you for logging in again.'}")
users_name.pop()
users_name.pop()
users_name.pop()
users_name.pop()
if(users_name==[]):
    print("We need to find some users.")
'''

# 5.10
'''
current_users=['Zhangsan','wangwu','lisi','ZHAOLIU','xieqi']
new_users=['zhangsan','zhaoliu','hehui','liuyuan','xieyan']
for user_1 in new_users:
    for old_user in current_users:
        if(user_1.lower()==old_user.lower()):
            print("Please input new name.")
            break
    if(old_user=='xieqi'):
        print("This name is not used.")
'''
# 5.11
'''
number_list=list(range(1,10))
for number in number_list:
    if(number==1):
        print("1st")
    elif(number==2):
        print("2nd")
    elif(number==3):
        print("3rd")    
    elif(number==4):
        print("4th")    
    elif(number==5):
        print("5th")
    elif(number==6):
        print("6th")
    elif(number==7):
        print("7th")
    elif(number==8):
        print("8th")
    elif(number==9):
        print("9th")

'''
