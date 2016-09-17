# ln_path = '/Users/raoweibo/last_name.txt'
# fn_path = '/Users/raoweibo/first_name.txt'
#
# fn = []
# ln1 = [] # 单字名
# ln2 = [] # 双字名

fn = ('李', '王', '张', '刘', '陈')
ln1 = ('兰', '正', '波', '立', '峰')
ln2 = ('志明', '志杰', '志军', '志立', '志宏')
nn = ('Mike', 'Tom', 'Coco', 'Kate', 'Bob')

# with open(fn_path,'r') as f:
#     for line in f.readline():
#         fn.append(line.split('\n')[0])


print(fn)

# with open(ln_path,'r') as f:
#     for line in f.readlines():
#         if len(line.split('\n')[0]) == 1:
#             ln1.append(line.split('\n')[0])
#         else:
#             ln2.append(line.split('\n')[0])

# print(ln1)
# print('='*70)
# print(ln2)
#
import random
#
# class FakeUser:
#     def fake_name(self,one_word=False,two_words=False):
#         if one_word:
#             full_name = random.choice(fn)+random.choice(ln1)
#         elif two_words:
#             full_name = random.choice(fn)+random.choice(ln2)
#         else:
#             full_name = random.choice(fn)+random.choice(ln1+ln2)
#         print(full_name)
#         def fake_gender(self):
#             gender = random.choice(['男', '女', '未知'])
#             print(gender)
#
# class SnsUser(FakeUser):
#     def get_followers(self,few=True,a_lot=False):
#         if few:
#             followers = random.randrange(1,50)
#         elif a_lot:
#             followers = random.randrange(200,400)
#         print(followers)
#
# user_a = FakeUser()
# user_b = SnsUser()
# user_a.fake_name()
# user_b.get_followers(few=True)

class FakeUser():
    def fake_name(self,amount=1,one_word=False,two_words=False):
        n = 0
        while n <= amount:
            if one_word:
                full_name = random.choice(fn)+random.choice(ln1)
            elif two_words:
                full_name = random.choice(fn)+random.choice(ln2)
            else:
                full_name = random.choice(fn)+random.choice(ln1+ln2)
            yield full_name
            n += 1
    def fake_gender(self,amount=1):
        n = 0
        while n <= amount:
            gender = random.choice(['男', '女', '未知'])
            yield gender
            n += 1

class SnsUser(FakeUser):
    def get_followers(self,amount=1,few=True,a_lot=False):
        n = 0
        while n <= amount:
            if few:
                followers = random.randrange(1,50)
            elif a_lot:
                followers = random.randrange(200,1000)
            yield followers
            n += 1
    def get_nick_name(self,amount=1):
        n = 0
        while n <= amount:
            nick_name = random.choice(nn)
            yield nick_name
            n += 1

user_a = FakeUser()
user_b = SnsUser()
for name in user_a.fake_name(5,two_words=True):
    print(name)
for gender in user_a.fake_gender(5):
    print(gender)
for nick_name in user_b.get_nick_name(5):
    print(nick_name)