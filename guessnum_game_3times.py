# -*- coding: utf-8 -*-
import random

num_mix = 1
num_max = 10

print('歡迎來到猜數字遊戲')
print(f'謎底為{num_mix}-{num_max}隨機的一個整數(最多五次猜測機會)')


gusscoun = 0
boom = random.randint(num_mix, num_max)
print(boom)

while True:
    gusscoun += 1
    if gusscoun >= 6:
        print(f'你輸了~超出猜測次數\n謎底為{boom}')
        break
    print(f'第{gusscoun}次猜測')
    user_guss = input('請輸入猜測的數字:')
    if user_guss.isdigit():
        user_guss = int(user_guss)
    else:
        print('只能是整數')
        continue
    if user_guss < boom:
        num_mix = user_guss
        print(f'{num_mix}-{num_max}之間')
    elif user_guss > boom:
        num_max = user_guss
        print(f'{num_mix}-{num_max}之間')  
    else: #user_guss == boom:
        print('恭喜你猜對了')
        break

