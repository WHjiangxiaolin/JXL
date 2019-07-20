#打印随机的8位密码

from random import choice    
from string import ascii_letters, digits

chs = ascii_letters + digits   #将字符和数字合并

def gen_pass(n=8):     #默认不加参数打印8位随机数
    result = ''

    for i in range(n):
        ch = choice(chs)
        result += ch

    return result

if  __name__ == '__main__':
    pw = gen_pass()
    print(pw)
    print(gen_pass(4))  #加参数,可以打印4位随机数
