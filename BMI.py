# -*- coding: utf-8 -*-
h = float( input('請輸入你的身高(M): '))
w = float( input('請輸入你的體重(KG): '))
bmi = w / (h**2)
print('您的BMI值是：',str(int(bmi)))
if bmi < 18.5:
    print('低于18.5：过轻')
elif bmi >= 18.5  and bmi < 25:
    print('18.5-25：正常偏瘦')
elif bmi >= 25  and bmi < 28:
    print('25-28：过重')
elif bmi >= 28  and bmi < 32:
    #print(str(int(bmi)) +'28-32：肥胖')
    print ('28-32：肥胖')
else: 
    print('高于32：严重肥胖')
