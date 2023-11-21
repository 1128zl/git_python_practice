#第五题：

'''
MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', 
              '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', 
              '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', 
              '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
              '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', 
              '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', 
              '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', 
              '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', 
              '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', 
              '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

def decode_bits(bits):
    split_bits = []
    morse_code = []

    last_bit = bits[0]
    start_index = 0

    for i, bit in enumerate(bits):
        if bit != last_bit:
            split_bits.append(bits[start_index:i])
            start_index = i        
        last_bit = bit
        
    split_bits.append(bits[start_index:])
    print('split_bits:', split_bits)
    
    if '0' in split_bits[0]:
        del split_bits[0]
        
    if '0' in split_bits[-1]:
        del split_bits[-1]
    
    time_unit = len(min(split_bits, key=len))
    print('time_unit:', time_unit)

    for item in split_bits:
        if '1' in item and len(item) < time_unit * 3:
            morse_code.append('.')
        elif '1' in item and len(item) >= time_unit * 3:
            morse_code.append('-')
        elif '0' in item and len(item) < time_unit * 3:
            morse_code.append('')
        elif '0' in item and len(item) < time_unit * 7:
            morse_code.append(' ')
        elif '0' in item and len(item) >= time_unit * 7:
            morse_code.append('   ')    
    
    print('morse_code:', morse_code)
    return ''.join(morse_code)


def decode_morse(morseCode):
    words_codes = ''.join(morseCode).split('   ')
    print('words_codes:', words_codes)
    
    letters_codes = [ word.split(' ')  for word in words_codes]
    letters = [ [MORSE_CODE[code] for code in word if code] for word in letters_codes]
    return ' '.join([ ''.join(letter) for letter in letters])
'''





#第四题：

'''
def fillable(stock, merch, n):
    # Your code goes here.
    #遍历保存所有商品种类和库存数量的字典
    for name,count in stock.items():
        
        #当库存有指定购买的商品并且数目大于等于购买数量
        if(name==merch and count>=n):
            return True

        #当库存有指定购买的商品并且数目小于购买数量   
        elif (name==merch and count<n):
            return False

    #当库存没有指定购买的商品  
    return False
'''

#第三题

'''

#转换的查询字典
PROTEIN_DICT = {
    'UUC': 'F', 'UUU': 'F',
    # Leucine
    'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    # Isoleucine
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    # Methionine
    'AUG': 'M',
    # Valine
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    # Serine
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
    # Proline
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    # Threonine
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    # Alanine
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    # Tyrosine
    'UAU': 'Y', 'UAC': 'Y',
    # Histidine
    'CAU': 'H', 'CAC': 'H',
    # Glutamine
    'CAA': 'Q', 'CAG': 'Q',
    # Asparagine
    'AAU': 'N', 'AAC': 'N',
    # Lysine
    'AAA': 'K', 'AAG': 'K',
    # Aspartic Acid
    'GAU': 'D', 'GAC': 'D',
    # Glutamic Acid
    'GAA': 'E', 'GAG': 'E',
    # Cystine
    'UGU': 'C', 'UGC': 'C',
    # Tryptophan
    'UGG': 'W',
    # Arginine
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    # Glycine
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    # Stop codon
    'UAA': 'Stop', 'UGA': 'Stop', 'UAG': 'Stop'
}

def protein(rna):
    #定义一个字符串用来保存结果
    pro = ""
    i = 0
    while i < len(rna):

        #每次取三个来找寻要替换的字符
        m = rna[i:i + 3]

        if m in PROTEIN_DICT:
            value = PROTEIN_DICT[m]

            #出现stop时停止转换
            if value == 'Stop':
                break
            pro += value
        i += 3
    #返回转换结果
    return pro

'''

#第二题

'''
def get_pins(observed):
    # 定义键盘数字的布局
    keyboard = {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9'],
        '0': ['0']
    }
    
    # 初始化结果列表
    result = ['']
    
    # 遍历观察到的PIN码中的每个数字
    for digit in observed:
        # 为每个数字的变化创建新的结果
        new_result = []
        for combination in result:
            for neighbor in keyboard[digit]:
                new_result.append(combination + neighbor)
        result = new_result

    return result
    
'''

#第一题

'''
def naughty_or_nice(data):
    count1=0
    count2=0
    #首先进入每个月
    for value1 in data:
        #访问字典格式进入每个月的nice ，naughty情况
        for value2,value3 in data[value1].items() :
            if(value3=='Nice'):
                count1+=1
            else:
                count2+=1
    #判断返回值
    if(count1>=count2):
        return "Nice!"
    else:
        return "Naughty!"
'''