#第一题

'''
def spin_words(sentence):
    # Your code goes here
    words=sentence.split()
    for index in range(len(words)):
        if(len(words[index])>=5):
            words[index]=words[index][::-1]
    sentence=" ".join(words)
    return sentence
'''

#第二题

'''
def find_outlier(integers):
    length = len(integers)

    if integers[0] % 2 == 0 and integers[1] % 2 == 0:
        for index in range(2, length):
            if integers[index] % 2 != 0:
                return integers[index]
        
    elif integers[0] % 2 == 0 and integers[1] % 2 != 0:
        if integers[2] % 2 == 0:
            return integers[1]
        else:
            return integers[0]
    
    elif integers[0] % 2 != 0 and integers[1] % 2 == 0:
        if integers[2] % 2 == 0:
            return integers[0]
        else:
            return integers[1]
    
    else:
        for index in range(2, length):
            if integers[index] % 2 == 0:
                return integers[index]
                
    return None

'''

#第三题

'''
def is_pangram(s):
    s = s.lower()
    letters = set()

    for c in s:
        if c.isalpha():
            letters.add(c)
    if(len(letters) == 26):
        return True
    return False
'''

#第四题

