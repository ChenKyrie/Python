# -*- coding: utf-8 -*-
import random
numMix = 1
numMax = 10

a = random.randint(numMix, numMax)
print(a)

num1 = None

while num1 != a:
    num1 = int(input('請輸入{numMix}-{numMax}的數:'.format(numMix=numMix,numMax=numMax)))
    if num1 > a:
        numMax = num1
    elif num1 < a:
        numMix = num1
    print(numMix,'-',numMax,'之間')
print('猜對了')
