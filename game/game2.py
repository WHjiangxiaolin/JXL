#石头/剪刀/布 游戏

import random
computer = random.choice(['石头','剪刀','布'])
player = input('石头/剪刀/布: ')
print('电脑出的是:'+computer)

if computer == player:
    print('平局')
elif computer == '石头' and player == '布':
    print('你赢了')
elif computer == '剪刀' and player == '石头':
    print('你赢了')
elif computer == '布' and player == '剪刀':
    print('你赢了')
else:
    print('你输了')
