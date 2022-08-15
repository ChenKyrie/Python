# -*- coding: utf-8 -*-
import random

#定義兩個數最大跟最小值
numMix = 1
numMax = 10

#運用函數隨機取值賦予變數a
a = random.randint(numMix, numMax)
#測試得知隨機數是多少
print(a)

#定義變數None
num1 = None

#只要用戶猜錯就進入while直到猜對為止
while num1 != a:
    num1 = int(input('請輸入{numMix}-{numMax}的數:'.format(numMix=numMix,numMax=numMax)))
#如果輸入值比較大,最大範圍改成輸入值
    if num1 > a:
        numMax = num1
#如果輸入值比較小,最小範圍改成輸入值
    elif num1 < a:
        numMix = num1
    print(numMix,'-',numMax,'之間')
print('猜對了')
