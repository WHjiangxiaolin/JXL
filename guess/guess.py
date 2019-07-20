#猜数字游戏

import random

num = random.randint(1,100)
running = True

while running:   #当条件为真时才运行循环
    number = int(input('请输入0-100的数字: '))
    if number > num:
        print('你猜大了')
    elif number < num:
        print('你猜小了')
    else:
        print('恭喜,你猜对了')
        running = False    #猜对了条件为假,会退出循环
