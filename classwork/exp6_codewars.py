#第一题

'''
def count_developers(lst):
    # Your code here
    signal=0
    for i in range(len(lst)):
        for key,value in lst[i].items():
            if key=='continent' and value=='Europe':
                signal+=1
            if key== 'language' and value=='JavaScript':
                signal+=1
        if signal==2:
            return 1
    return 0
    pass
'''

#第二题

'''
def zero(func=None): 
    if func==None:
        return 0
    else :
        return func(0)

def one(func=None): 
    if func==None:
        return 1
    else :
        return func(1)
def two(func=None): 
    if func is None:
        return 2
    else :
        return func(2)
#your code here
def three(func=None):
    if func is None:
        return 3
    else :
        return func(3)
def four(func=None): 
    if func is None:
        return 4
    else :
        return func(4)
    
def five(func=None): 
    if func is None:
        return 5
    else :
        return func(5)
    
def six(func=None): 
    if func is None:
        return 6
    else :
        return func(6)
def seven(func=None): 
    if func is None:
        return 7
    else :
        return func(7)
    
def eight(func=None): 
    if func is None:
        return 8
    else :
        return func(8)
def nine(func=None): 
    if func is None:
        return 9
    else :
        return func(9)

def plus(y): 
    return lambda x: x + y
def minus(y): 
    return lambda x: x - y
def times(y):
    return lambda x: x * y
def divided_by(y):  
    return lambda x: x / y

'''
#第三题

'''
def shorten_number(suffixes, base):
    def filter1(input):
        if isinstance(input, str) and input.isdigit():
            number=int(input)
            count=0
            while(number>=base):
                number/=base
                count+=1
            return '{:.0f}{}'.format(number, suffixes[count])
        else:
            return str(input)
    return filter1

'''




#第四题

'''
def find_senior(lst): 
    # your code here
    result=[]
    result.append(lst[0])
    mage=lst[0]['age']
    for i in range(1,len(lst)):
        for key,value in lst[i].items():
            if key=='age' and value>mage:
                result=[]
                result.append(lst[i])
            elif key=='age' and value==mage:
                result.append(lst[i])
            
    return result
    pass
'''


#第五题

#(部分通过)

'''
def curry_partial(f, *initial_args):
    """ Curries and partially applies the initial arguments to the function """
    if len(initial_args) >= f.__code__.co_argcount:
        return f(*initial_args)
    else:
        return lambda *more_args: curry_partial(f, *(initial_args + more_args))
'''