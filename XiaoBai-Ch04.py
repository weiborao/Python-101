# 摄氏温度转华氏温度
# def fahrenheit_converter(C):
#     fahrenheit = round(C * 9/5 + 32,2)
#     return str(fahrenheit) + '˚F'
#
# temp_c = float(input('Please input your Temperature of ˚C:'))
# temp_f = fahrenheit_converter(temp_c)
# print ('the fahrenheit temperature is '+str(temp_f))

# 练习题1,设计一个重量转换器,输入以"g"为单位的数字,返回"kg"的结果

# def g2kg(input1):
#     output =  round(input1 / 1000, 2)
#     return str(output) + ' kg'
#
# g = int(input('Please input your weight of g:'))
# kg = g2kg(g)
# print ('Translate to '+kg)

# 练习题2,设计一个求直角三角形斜边长的函数

# def calc_lenth(input1,input2):
#     output = round(((input1 * input1) + (input2 * input2)) ** (1./2), 2)
#     return str(output)
#
# short_1 = int(input('Please input the short side:'))
# short_2 = int(input('Please input the short side:'))
# long_3 = calc_lenth(short_1,short_2)
# print(long_3)

# import math
#
# def calc_lenth(x,y):
#     # output = round(((x * x) + (y * y)) ** (1./2), 2)
#     # output = round(math.sqrt((x * x) + (y * y)),2)
#     # return str(output)
#     return 'The right triangle third side\'s lenth is {}'.format((x**2 + y**2)**(1/2))
#
# short_1 = int(input('Please input the short side:'))
# short_2 = int(input('Please input the short side:'))
# long_3 = calc_lenth(short_1,short_2)
# print(long_3)

# def trapezoid_area(base_up,base_down,height):
#     return 1/2 * (base_up + base_down) * height
#
# print(trapezoid_area(1,2,3))
#
# base_up = 1
# base_down = 2
# height = 3
#
# print(trapezoid_area(height,base_down,base_up))


print('  *', ' * *', '* * *', '  |  ', sep='\n')


def text_create(name, msg):
    user_path = '/Users/raoweibo/'
    full_path = user_path + name + '.txt'
    myfile = open(full_path, 'w')
    myfile.write(msg)
    myfile.close()
    print('Done')
#
# text_create('hellopython','Hello this is the test generate by Python')

# def divide_mod(num1, num2):
#     return str(num1) + '÷' + str(num2) + ' = ' + str(num1 // num2) + ' 余 ' + str(num1 % num2)
#
# print(divide_mod(1839 , 29))

def text_filter(word, censored_word = 'lame', changed_word = 'Awesome'):
    return word.replace(censored_word,changed_word)

print(text_filter('Python is lame!'))

def censored_text_create(name,msg):
    clean_msg = text_filter(msg)
    text_create(name,clean_msg)

censored_text_create('Try','lame!lame!lame!')