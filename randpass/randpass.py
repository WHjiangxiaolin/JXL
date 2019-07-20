#打印随机的8位密码

from random import choice

chs = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
result = ''

for i in range(8):
    ch = choice(chs)
    result += ch

print(result)
