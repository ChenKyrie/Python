import random

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
options = ['s','r','p']
user_cho = input('請輸入字母 s(剪刀) r(石頭) p(布)')
compter_cho = options[random.randint(0, 2)]

print('你出')
if user_cho == 's':
    print(scissor)
elif user_cho == 'r':
    print(rock)
else:
    print(paper)


print('電腦出')
if compter_cho == 's':
    print(scissor)
elif compter_cho == 'r':
    print(rock)
else:
    print(paper)

if (user_cho == 's' and compter_cho == 'p') or\
    (user_cho == 'r' and compter_cho == 's') or\
    (user_cho == 'p' and compter_cho == 'r'):
    print('恭喜你贏了!')
elif (user_cho == 's' and compter_cho == 's') or\
    (user_cho == 'r' and compter_cho == 'r') or\
    (user_cho == 'p' and compter_cho == 'p'):
    print('平手~')
else:
    print('你輸了!')
