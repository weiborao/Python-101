# -*- coding: utf-8 -*-
import string


pass_chars = string.printable
numbers = pass_chars[:10]
lower_case = pass_chars[10:36]
cap_case = pass_chars[36:62]
punctuation_words = pass_chars[62:95]


def is_num(the_char):
    # 判断是否为数字字符
    if the_char in numbers:
        return True
    else:
        return False


def is_lower_case(the_char):
    # 判断是否为小写字母
    if the_char in lower_case:
        return True
    else:
        return False


def is_cap_case(the_char):
    # 判断是否为大写字母
    if the_char in cap_case:
        return True
    else:
        return False


def is_punctuation_words(the_char):
    # 判断是否为大写字母
    if the_char in punctuation_words:
        return True
    else:
        return False


active = True
filename = "good_passwords.txt"

try:
    with open(filename, "w") as f_obj:
        contents = f_obj.write("")
except FileExistsError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

while active:
    num_nums = 0
    num_lower = 0
    num_cap = 0
    num_punctuation = 0
    your_pass = input("Please enter your password:")
    if your_pass != "q":
        if len(your_pass) >= 8:
            for char in your_pass:
                if is_num(char):
                    num_nums += 1
                elif is_lower_case(char):
                    num_lower += 1
                elif is_cap_case(char):
                    num_cap += 1
                elif is_punctuation_words(char):
                    num_punctuation += 1
            if num_nums == 0:
                print("Password needs to contain numbers.")
            elif num_lower == 0:
                print("Password needs to contain lower case letters.")
            elif num_cap == 0:
                print("Password needs to contain cap case letters.")
            elif num_punctuation == 0:
                print("Password needs to contain punctuations")
            else:
                print("Good Passwords.")
                print("Numbers, " + str(num_nums))
                print("Lower Case, " + str(num_lower))
                print("Cap Case, " + str(num_cap))
                print("Punctuations, " + str(num_punctuation))
                with open(filename, 'a') as f_obj:
                    f_obj.write(your_pass + "\n")
        elif len(your_pass) < 8:
            print("Password should be longer than or equal to 8.")
    elif your_pass == "q":
        active = False
