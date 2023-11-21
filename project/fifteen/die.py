from random import randint

class Die:
    #创建一个骰子的类
    
    #初始化函数，定义属性
    def __init__(self,num_sides=6):
        
        self.num_sides=num_sides
    
    #表示扔骰子功能的函数,返回扔骰子所显示的数
    def roll(self):
        return randint(1,self.num_sides)
    