# Write the configuration to Folder

# myfile = open('/Users/raoweibo/config.txt', 'w')
# for i in range(10, 70):
#     j = str(i)
#     myfile.write('interface TenGigE 0/0/0/1.' + j + '\n')
#     myfile.write(' encapsulation dot1q ' + j + '\n')
#     myfile.write(' ipv4 address 190.168.' + j + '.1 255.255.255.0' + '\n')
#     myfile.write(' no shutdown\n\n')
# myfile.close()

# 以下代码来自编程小白


what_he_does = ' plays '
his_instrument = 'guitar'
his_name = 'Robert Johnson'
artist_intro = his_name + what_he_does + his_instrument
print(artist_intro)

words = 'words' * 3
print(words)

word = 'a looooooog word'
num = 12
string = 'Bang!'
total = string * (len(word) - num)
print (total)

name = 'My name is Mike'
print (name[0:4])
print(name[-4])
print(name[11:14])
print(name[11:15])
print(name[5:])
print(name[:5])

word = 'friends'
find_the_evil_in_your_frieds = word[0]+word[2:4]+word[-3:-1]
print (find_the_evil_in_your_frieds)

myurl = 'http://www.cisco.com/img/1432didkfa355djsfdfa.jpg'
file_name1 = myurl[-10:]
print (file_name1)
file_name2 = myurl[:-16]+myurl[-4:]
print (file_name2)
print (myurl[-4:])

phone_number = '1386-666-0006'
hidding_number = phone_number.replace(phone_number[:9], '*' * 9)
print(hidding_number)

print('{} a word she can get what she {} for.'.format('With', 'came'))
print('{preposition} a word she can get what she {verb} for'.format(preposition = 'With',verb = 'came'))
print('{0} a word she can get what she {1} for.'.format('With','came'))

city = input("write down the name of city:")
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)
print(url)