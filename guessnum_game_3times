# -*- coding: utf-8 -*-
import random

#定義變數最大最小值
numMix = 1
numMax = 10

#i值讓while跑次數用
i = 3

#用random函數生成隨機數介於兩個變數之間
a = random.randint(numMix, numMax)

#測試先得知a值
print(a)

#定義None進入while迴圈
num1 = None

#while處理猜錯並且次數>0
while num1 != a and i > 0 :
    
    #讓用戶輸入值 = num1,使用format賦予變數更靈活取得值還有剩餘次數
    num1 = int(input('請輸入{numMix}-{numMax}的數,剩餘{i}次機會:'.format(numMix=numMix,numMax=numMax,i=i)))
    #次數每次迴圈都減1
    i -= 1
    #只要用戶輸入值大於a,更動numMax值.縮小範圍
    if num1 > a :
        numMax = num1
        #print(numMix,'-',numMax,'之間')
    #只要用戶輸入值小於a,更動numMax值.縮小範圍
    elif num1 < a :
        numMix = num1
        #print(numMix,'-',numMax,'之間')
print('----------------------------------------')    

#if處理結果
if num1 == a :
    print('恭喜你猜對了答案是',a)
else :
    print('次數用完了!答案是',a)
