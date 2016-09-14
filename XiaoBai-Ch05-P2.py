cn_mobile = [134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,187,188,147,178,1705]
cn_union = [130,131,132,155,156,185,186,145,176,1709]
cn_telecom = [133,153,180,181,189,177,1700]


# def is_valid(input_str):
#     if len(input_str) == 11:
#         return True
#     else:
#         return False
#
#
# def which_vendor(input_str):
#     prefix_num1 = input_str[0:3]
#     prefix_num1 = int(prefix_num1)
#     prefix_num2 = input_str[0:4]
#     prefix_num2 = int(prefix_num2)
#     if (prefix_num1 in cn_mobile) + (prefix_num2 in cn_mobile):
#         return 0
#     elif (prefix_num1 in cn_union) + (prefix_num2 in cn_union):
#         return 1
#     elif (prefix_num1 in cn_telecom) + (prefix_num2 in cn_telecom):
#         return 2
#     else:
#         return 101
#
#
# def input_phone_num():
#     vendor_list = ['China Mobile','China Unicom','China Telecom']
#     input_str = input('Enter your number:')
#     if is_valid(input_str):
#         vendor_index = which_vendor(input_str)
#         if vendor_index < 3:
#             print('Operator : '+vendor_list[vendor_index])
#             print("We\'re sending verification code via text to your phone:{}".format(input_str))
#         else:
#             print('No such an operator.')
#             input_phone_num()
#     else:
#         print('Invalid length, your number should be in 11 digits.')
#         input_phone_num()
#
#
# input_phone_num()


def is_valid(input_str):
    if len(input_str) == 11:
        return True
    else:
        return False


def which_vendor(input_str):
    prefix_num1 = input_str[0:3]
    prefix_num1 = int(prefix_num1)
    prefix_num2 = input_str[0:4]
    prefix_num2 = int(prefix_num2)
    if (prefix_num1 in cn_mobile) + (prefix_num2 in cn_mobile):
        return 'China Mobile'
    elif (prefix_num1 in cn_union) + (prefix_num2 in cn_union):
        return 'China Unicom'
    elif (prefix_num1 in cn_telecom) + (prefix_num2 in cn_telecom):
        return 'China Telecom'
    else:
        return '101'


def input_phone_num():
    input_str = input('Enter your number:')
    the_vendor = which_vendor(input_str)
    if is_valid(input_str):
        if which_vendor(input_str) != 3:
            print('Operator : '+the_vendor)
            print("We\'re sending verification code via text to your phone:{}".format(the_vendor))
        else:
            print('No such an operator.')
            input_phone_num()
    else:
        print('Invalid length, your number should be in 11 digits.')
        input_phone_num()


input_phone_num()