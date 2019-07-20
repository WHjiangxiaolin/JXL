#石头/剪刀/布 游戏

import random

all_choices = ['石头','剪刀','布']
win_lis = [['石头','剪刀'], ['剪刀','布'], ['布','石头']]  #你赢的3种情况
prompt = '''(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): '''

computer = random.choice(all_choices)
ind = int(input(prompt))
player = all_choices[ind]   #在列表中取出下标对应的字符串

print("Your choice: %s, Computer's choice: %s" % (player, computer))
if player == computer:
    print('\033[32;1m平局\033[0m')  #打印的字有颜色
elif [player, computer] in win_lis:
    print('\033[31;1mYou Win!!!\033[0m')
else:
    print('\033[31;1mYou Lose!!!\033[0m')
