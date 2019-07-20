#用户输入用户名和密码进行登录,如果用户名不存在可以注册

import getpass

userdb = {}

def register():
    username = input('请输入用户名: ')
    if username in userdb:
        print('\033[31;1m用户名已存在\033[0m')
    else:
        password = input('请输入密码: ')
        userdb[username] = password    #将用户名和密码写入字典保存,键是用户名,值是密码

def login():
    username = input('请输入用户名: ')
    password = getpass.getpass('请输入密码: ')
    # password = input('请输入密码: ')
    if userdb.get(username) == password:    #如果输入的密码和输入的用户名在字典中取值相同,则表示登录成功
        print('\033[32;1m登录成功\033[0m')
    else:
        print('\033[31;1m登录失败\033[0m')

def show_menu():
    cmds = {'0': register, '1':login}
    prompt = """(0) 注册
(1) 登录
(2) 退出
请选择(0/1/2): """

    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2']:
            print('无效的输入,请重试.')
            continue     #如果输入的不是0/1/2,则提示,并重新循环

        if choice == '2':
            print('bye-bye')
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()


