import sys
import subprocess
from string import ascii_letters,digits
from random import choice

all_chs = ascii_letters + digits

def gen_pass(n=8):
    # 列表解析,取出n个字符放到列表中
    srt_list = [choice(all_chs) for i in range(n)]
    # 用空串将列表中的字符拼接
    return ''.join(srt_list)

def add_user(username, password, fname):
    info = """用户信息:
用户名: %s
密码: %s
    """ % (username, password)

    # 首先判断用户是不是已存在
    result = subprocess.run('id %s &> /dev/null' % username, shell=True)
    if result.returncode == 0:
        print('%s用户已存在' % username)
        return   # return默认返回None，程序遇到return就结束并返回了

    # 创建用户，并设置密码
    subprocess.run(
        'echo %s | passwd --stdin %s' % (password, username),
        shell=True,
        stdout=subprocess.PIPE,     #通过管道将输出存在标准输出中
        stderr=subprocess.PIPE      #通过管道将输出存在标准错误中
    )
    # 将用户信息写入文件
    with open(fname, 'a') as fobj:
        fobj.write(info)

if __name__ == '__main__':
    username = sys.argv[1]   #运行程序时输入参数
    password = gen_pass()
    fname = '/tmp/users.txt'
    rc = add_user(username, password, fname)
    print(rc)
