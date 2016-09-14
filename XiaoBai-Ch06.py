# 本章学习数据结构
'''
list = [val1,val2,val3,val4]
dict = {key1:val1,key2:val2}
tuple = (val1,val2,val3,val4)
set = {val1,val2,val3,val4}
'''

# 列表

Weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print(Weekday[0])

fruit = ['pineapple','pear']
fruit.insert(1,'grape')
print(fruit)

fruit [0:0] = ['Orange']
print(fruit)

fruit.remove('grape')
print(fruit)

fruit[0] = 'Grapefruit'
print(fruit)

del fruit[0:2]
print(fruit)

periodic_table = ['H','He','Li','Be','B','C','N','O','F','Ne']
print(periodic_table[0])
print(periodic_table[-2])
print(periodic_table[0:3])
print(periodic_table[-10:-7])
print(periodic_table[-10:])
print(periodic_table[:9])

# 字典

NASDAQ_code = {
    'BIDU':'Baidu',
    'SINA':'Sina',
    'YOKU':'Youku'
}

print(NASDAQ_code)
NASDAQ_code.update({'FB':'Facebook','TSLA':'Tesla'})
print(NASDAQ_code)
del NASDAQ_code['FB']
print(NASDAQ_code)
print(NASDAQ_code['TSLA'])

# 元组

letters = ('a','b','c','d','e','f','g')
print(letters)
print(letters[0])

# 集合

a_set = {1,2,3,4}
a_set.add(5)
print(a_set)
a_set.discard(5)
print(a_set)

num_list = [6,2,7,4,1,3,5]
print(sorted(num_list))
print(sorted(num_list,reverse=True))

str = ['a','b','c','d','e','f','g']
num = [1,2,3,4,5,6,7]
for a,b in zip(num,str):
    print(b,'is',a)

# 推导式

a = []
for i in range(1,11):
    a.append(i)

b = [i for i in range(1,11)]

import time


a = []
t0 = time.clock()
for i in range(1,2000000):
    a.append(i)
print(time.clock() - t0, 'seconds process time')

t0 = time.clock()
b = [i for i in range(1,2000000)]
print(time.clock() - t0, 'seconds process time')

a = [i**2 for i in range(1,10)]
c = [j+1 for j in range(1,10)]
k = [n for n in range(1,10) if n % 2 ==0]
z = [letter.lower() for letter in 'ABCDEFGHIJKLMN']
print (a,c,k,z,sep='\n')

d = {i:i+1 for i in range(4)}
g = {i:j for i,j in zip(range(1,6),'abcde')}
j = {i:j.upper() for i,j in zip(range(1,6),'abced')}
print(d,g,j,sep='\n')

letters = ['a','b','c','d','e','f','g']
for num,letter in enumerate(letters):
    print(letter,'is',num+1)

lyric = 'The night begin to shine , the night begin to shine'
words = lyric.split()
words = set(words)
print(words)

# path = '/Users/raoweibo/Walden.txt'
# with open(path,'r') as text:
#     words = text.read().split()
#     print(words)
#     for word in words:
#         print('{} -{} times'.format(word,words.count(word)))

import string

path = '/Users/raoweibo/Walden.txt'

with open(path,'r') as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index = set(words)
    counts_dict = {index:words.count(index) for index in words_index}

for word in sorted(counts_dict,key=lambda x:counts_dict[x],reverse=True):
    print('{} -- {} times'.format(word,counts_dict[word]))