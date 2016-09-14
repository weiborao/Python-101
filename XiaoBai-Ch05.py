# >>> 1>2
# False
# >>> 1<2<3
# True
# >>> 42 != '42'
# True
# >>> 'Name' == 'name'
# False
# >>> 'M' in 'Magic'
# True
# >>> number = 12
# >>> number is 12
# True

# 第五章主要学习循环与判断
"""
成员运算符:
in 测试前者是否存在于in后面的集合中;
列表,创建一个列表
album = []

is 表示身份鉴别的布尔运算符。

"""
# album = ['Black Star', 'David Bowie', 25, True]
#
# password_list =[0,'12345']
# def account_login(max_wrong_time):
#     password = input('Password:')
#     password_list.append(password)
#     if password_list[-1] == password_list[1]:
#         print ('Login success!')
#     elif len(password_list) != max_wrong_time + 2:
#         password_list[0] += 1
#         print ('Wrong password or invalid input!')
#         account_login(max_wrong_time)
#     else:
#         password_list[0] += 1
#         print ('You have entered wrong password for {} times, exit!'.format(max_wrong_time))

# 调用函数
# account_login(3)
# print ('You have entered:\n')
# print(password_list[2:])

# 新的代码
# password_list = ['*#*#', '12345']
# def account_login():
#     password = input ('Password:')
#     password_correct = password == password_list [-1]
#     password_reset = password == password_list [0]
#     if password_correct:
#         print('Login success!')
#     elif password_reset:
#         new_password = input ('Enter a new password:')
#         password_list.append(new_password)
#         print('Your password has changed successfully!')
#         account_login()
#     else:
#         print('Wrong password or invalid input!')
#         account_login()

# account_login()

# for 循环

# for every_letter in "Hellow World!":
#     print (every_letter)

# songslist = ['Holy Diver', 'Thunderst ruck', 'Rebel Rebel']
# for song in songslist:
#     if song == 'Holy Diver':
#         print (song,'- Dio',sep='\t\t|\t')
#     elif song == 'Thunderst ruck':
#         print (song, '- AC/DC',sep='\t|\t')
#     elif song == 'Rebel Rebel':
#         print (song, '- David Bowie',sep='\t\t|\t')

# 以下循环打印9x9乘法表

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()


# 用户登录程序

# password_list = ['*#*#', '12345']


# def account_login():
#     tries = 3
#     while tries > 0:
#         password = input('Password:')
#         password_correct = password == password_list[-1]
#         password_reset = password == password_list[0]
#         if password_correct:
#             print('Login success!')
#             break
#         elif password_reset:
#             new_password = input('Enter a new password:')
#             password_list.append(new_password)
#             print('Your password has changed successfully!')
#             account_login()
#         else:
#             print('Wrong password or invalid input!')
#             tries -= 1
#             print(tries, 'times left')
#     else:
#         print('Your account has been suspended')
#
#
# account_login()

# 练习题1,在目录中创建10个文件,以1-10命名。

# def file_create(name, msg):
#     user_path = '/Users/raoweibo/'
#     full_path = user_path + name + '.txt'
#     myfile = open(full_path, 'w')
#     myfile.write(msg)
#     myfile.close()
#     print('Done ', name)


# for i in range(1,11):
#     file_create (str(i),'This is NO.{} file'.format(i))

# 练习题2,打印1-100内的偶数。

# for num in range (1,101):
#     if num % 2 == 0:
#         if num % 10 != 0:
#             print (num,end='\t')
#         else:
#             print(num)
# print()

# 练习题3,计算复利

# def invest(amount,rate,time):
#     print ('Principal amount: {}'.format(amount))
#     for i in range (1,time+1):
#         amount = amount * (1 + rate)
#         print ('Year {} : ${}'.format(i, round(amount , 2)))
#
# invest(100, 0.05 ,10)

# 趣味编程

# a_list = [1,2,3]
# print (sum(a_list))

# import random

# print ('<<<<< GAME START >>>>>')
# your_choice = input ('Big or Small:')
# print ('<<<< ROLE THE DICE! >>>>')
#
# point_list = [0,0,0]
# point_list[0] = random.randrange(1,7)
# point_list[1] = random.randrange(1,7)
# point_list[2] = random.randrange(1,7)
# print ('The points are {}'.format(point_list),end='\t')
#
# list_sum = sum(point_list)
#
# if 10 > list_sum > 3:
#     _result = 'Small'
# else:
#     _result = 'Big'
#
# if your_choice == _result:
#     print('You Won!')
# else:
#     print('You Lose!')

