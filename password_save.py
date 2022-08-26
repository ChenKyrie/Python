import json

def get_password_dic():
    with open('password.json','r') as f:
        password_str = f.read()
        if password_str == '':
            return {}
        else:
            return json.loads(f.read())

def check_name(name):
    password_dic = get_password_dic()
    if name in password_dic.keys():
        return False
    else:
        return True

def add_password(name, account, password):
    if check_name(name):
        password_dic = get_password_dic()
        password_dic[name] = {
            'account': account,
            'password': password
        }
        with open('password.json','w') as f:
            f.write(json.dumps(password_dic))
        return True
    else:
        return False

print('歡迎使用密碼管理器~')
while True:
    mode = input('請問要使用什麼功能呢? (r查詢 a新增 q離開)')
    if mode == 'q':
        break
    elif mode == 'a':
        name = input('請輸入帳號名稱:')
        account = input('請輸入帳號:')
        password = input('請輸入密碼:')
        if add_password(name, account, password):
            print('新增成功~')
        else:
            print('已有此帳號名稱')
    elif mode == 'r':
        name = input('請輸入帳號名稱:')
        if check_name(name):
            print('無此帳號名稱')
        else:
            password_dic = get_password_dic()
            account = password_dic[name]['account']
            password = password_dic[name]['password']
            print(f'帳號:{account}, 密碼:{password}')
