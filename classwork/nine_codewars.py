#第一题
'''
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    # Your code here
    
    def is_worth_it(self):
        if self.draft-(self.crew*1.5)>20:
            return True
        else :
            return False

Titanic=Ship(15,10)
Titanic.is_worth_it()
'''

#第二题
'''
class Block:
    
    def __init__(self,list):
        self.width=list[0]
        self.length=list[1]
        self.height=list[2]
        
    def get_width(self):
        return self.width

    def get_length(self):
        return self.length
    
    def get_height(self):
        return self.height
    
    def get_volume(self):
        return self.width*self.length*self.height
    
    def get_surface_area(self):
        return (self.height*self.width+self.width*self.length+self.length*self.height)*2
    
b=Block([2,4,6])
b.get_width()     
b.get_length() 
b.get_height()
b.get_volume()
b.get_surface_area() 
'''

#第三题
'''
# TODO: complete this class
import math
class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.c=collection
        self. i= items_per_page
        
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.c)
    
    # returns the number of pages
    def page_count(self):
        return math.ceil(len(self.c) / self.i)
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if len(self.c)-self.i*(page_index+1)>0:
            return self.i
        elif len(self.c)-self.i*(page_index+1)<0 and len(self.c)-self.i*(page_index)>0:
            return len((self.c))-self.i*(page_index)
        else :
            return -1
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if(item_index   <=0):
            return -1
        elif(item_index>len(self.c) or item_index<0):
            return -1
        else:
            return item_index//self.i
'''

#第四题
'''
class Vector:
    def __init__(self, elements):
        self.elements = elements

    def add(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must have the same length for addition")
        result = [x + y for x, y in zip(self.elements, other.elements)]
        return Vector(result)

    def subtract(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must have the same length for subtraction")
        result = [x - y for x, y in zip(self.elements, other.elements)]
        return Vector(result)

    def dot(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must have the same length for dot product")
        result = sum(x * y for x, y in zip(self.elements, other.elements))
        return result

    def norm(self):
        result = sum(x ** 2 for x in self.elements) ** 0.5
        return result

    def __str__(self):
        return f"Vector({self.elements})"

    def equals(self, other):
        if not isinstance(other, Vector):
            return False
        return self.elements == other.elements
'''

#第五题（部分通过）
'''
class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def validate_rank(self, rank):
        if rank not in [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]:
            raise ValueError("Invalid rank")

    def inc_progress(self, activity_rank):
        self.validate_rank(activity_rank)

        if self.rank == 8:
            return  # If user is already at the maximum rank, no progress can be made

        rank_difference = activity_rank - self.rank

        if rank_difference == 0:
            self.progress += 3
        elif rank_difference == -1:
            self.progress += 1
        elif rank_difference > 0:
            self.progress += 10 * rank_difference * rank_difference

        while self.progress >= 100:
            self.progress -= 100
            if self.rank < 8:
                self.rank += 1

        # Handle the case where the user goes from rank -1 to rank 1
        if self.rank == -1 and activity_rank == 1:
            self.rank += 2

        if self.rank == 8:
            self.progress = 0
'''


