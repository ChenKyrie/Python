import random
letters_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                 "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]

letters_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+"]

print('歡迎使用密碼產生器~')

upper_num = int(input('請問需要幾個大寫英文字母?'))
lower_num = int(input('請問需要幾個小寫英文字母?'))
number_num = int(input('請問需要幾個數字?'))
symbol_num = int(input('請問需要幾個符號?'))

password = ''
for i in range(0 ,upper_num):
    password += letters_upper[random.randint(0, 25)]

for i in range(0 ,lower_num):
    password += letters_lower[random.randint(0, 25)]

for i in range(0 ,number_num):
    password += numbers[random.randint(0, 9)]

for i in range(0 ,symbol_num):
    password += symbols[random.randint(0, 9)]

password_list = list(password)
random.shuffle(password_list)
new_password = ''
for char in password_list:
    new_password += char
print(new_password)
