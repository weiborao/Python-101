# 第一个示例:
# class CocoCola:
#     it_taste = 'So good!'
#
# coke_for_bum = CocoCola()
# coke_for_president = CocoCola()
# print(coke_for_bum.it_taste)
# print(coke_for_president.it_taste)
#
# class CocoCola:
#     formula = ['caffeine', 'sugar', 'water', 'soda']

# 第二个示例:
# coke_for_me = CocoCola()
# coke_for_you = CocoCola()
#
# print(CocoCola.formula)
# print(coke_for_me.formula)
# print(coke_for_you.formula)
#
# for element in coke_for_me.formula:
#     print(element)
#
# coke_for_China = CocoCola()
# coke_for_China.local_logo = '可口可乐'
#
# print(coke_for_China.local_logo)

# 第5节示例:

# class CocoCola:
#     formula = ['caffeine', 'sugar', 'water', 'soda']
#     def drink(self):
#         print('Energy!')
#
# coke = CocoCola()
# coke.drink()

# 第6节示例:

# class CocoCola:
#     formula = ['caffeine', 'sugar', 'water', 'soda']
#     def drink(self,how_much):
#         if how_much == 'a sip':
#             print('Cool~')
#         elif how_much == 'whole bottle':
#             print('Headache')
#
# ice_coke = CocoCola()
# ice_coke.drink('a sip')

# 第7节示例:

# class CocoCola:
#     formula = ['caffeine', 'sugar', 'water', 'soda']
#     def __init__(self):
#         self.local_logo = '可口可乐'
#     def drink(self):
#         print('Energy!')
#
# coke = CocoCola()
# print(coke.local_logo)


# class CocoCola:
#     formula = ['caffeine', 'sugar', 'water', 'soda']
#     def __init__(self):
#         for element in self.formula:
#             print('Coke has {}!'.format(element))
#
#     def drink(self):
#         print('Energy!')
#
# coke = CocoCola()

# class CocoCola:
#     formula = ['caffeine', 'sugar', 'water', 'soda']
#     def __init__(self,logo_name):
#         self.local_logo = logo_name
#
#     def drink(self):
#         print('Energy!')
#
# coke = CocoCola('可口可乐')
# coke.local_logo

# 第8节

# class CocaCola:
#     calories    = 140
#     sodium      = 45
#     total_carb  = 39
#     caffeine    = 34
#     ingredients = [
#         'High Fructose Corn Syrup',
#         'Carbonated Water',
#         'Phosphoric Acid',
#         'Natural Flavors',
#         'Caramel Color',
#         'Caffeine'
#     ]
#     def __init__(self,logo_name):
#         self.local_logo = logo_name
#
#     def drink(self):
#         print('You got {} cal energy, {} caffeine'.format(self.calories,self.caffeine))
#
# class CaffeineFree(CocaCola):
#     caffeine    = 0
#     ingredients = [
#         'High Fructose Corn Syrup',
#         'Carbonated Water',
#         'Phosphoric Acid',
#         'Natural Flavors',
#         'Caramel Color'
#     ]
#
# coke_a = CaffeineFree('Cocacola-FREE')
# coke_a.drink()
#
# class TestA:
#     attr = 1
#     def __init__(self):
#         self.attr = 42
# obj_a = TestA()
# print(obj_a.attr)
# print(TestA.__dict__)
# print(obj_a.__dict__)

from bs4 import BeautifulSoup
soup = BeautifulSoup
print(type(soup))
