# -*- coding: utf-8 -*-
import string
import random

pass_chars = string.printable
numbers = pass_chars[:10]
lower_case = pass_chars[10:36]
cap_case = pass_chars[36:62]
punctuation_words = "!#$%&*+,-;@~"
pass_chars = numbers + lower_case + cap_case + punctuation_words


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


def pass_gen(the_lenth=8):
    final_pass = ""
    for num in range(0, the_lenth, 1):
        final_pass += pass_chars[random.randint(0, len(pass_chars) - 1)]
    return final_pass


def pass_valiate():
    active = True
    the_passwords = ""
    while active:
        num_nums = 0
        num_lower = 0
        num_cap = 0
        num_punctuation = 0
        the_passwords = pass_gen()
        for char in the_passwords:
            if is_num(char):
                num_nums += 1
            elif is_lower_case(char):
                num_lower += 1
            elif is_cap_case(char):
                num_cap += 1
            elif is_punctuation_words(char):
                num_punctuation += 1
        if num_lower * num_nums * num_cap * num_punctuation == 0:
            active = True
        else:
            active = False
    return the_passwords

for i in range(0, 100):
    complex_password = pass_valiate()
    print(complex_password)
