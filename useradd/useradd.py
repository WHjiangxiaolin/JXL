#给系统创建用户并生成随机8位数密码,用户名和密码保存在指定的文件中,用户名如果存在提示

import subprocess   #可以在系统命令行运行命令的模块
from string import ascii_letters, digits
from random import choice

chs = ascii_letters + digits

def add_passwd():    #随机生成8位数密码
    passwd = ''
    for i in range(8):
        ch = choice(chs)
        passwd += ch

    return passwd

def add_user():
    while True:
        username = input('请输入用户名: ')
        rc = subprocess.run('id %s &> /dev/null' % username, shell=True)
        a = rc.returncode
        if not a == 0:   #判断用户是否存在,如果不为0,则表示用户不存在,创建用户和密码
            subprocess.run('useradd %s &> /dev/null' % username, shell=True)
            subprocess.run('echo %s | passwd --stdin %s &> /dev/null' % (passwd, username), shell=True)
            print('用户%s创建成功' % username)
            break
        print('用户已存在')    #反之用户存在则提示

    return username

def add_file():
    fname = input('请输入文件名: ')     #输入保存用户名和密码的文件

    return fname

def wfile(fname, username, passwd):
    with open(fname, 'a') as fobj:      #将用户名和密码保存到文件
        fobj.writelines(username + '\n')
        fobj.writelines(passwd + '\n')
    print('你的账号和密码存在%s文件中' % fname)

if __name__ == '__main__':
    passwd = add_passwd()
    username = add_user()
    fname = add_file()
    wfile(fname, username, passwd)


