import random
#石头\剪刀\布 游戏,赢2局

all_choices = ['石头','剪刀','布']
win_lis = [['石头','剪刀'], ['剪刀','布'], ['布','石头']]
prompt = '''(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): '''
Win = 0
Lose = 0
while Win < 2 and Lose < 2:
    computer = random.choice(all_choices)
    ind = int(input(prompt))
    player = all_choices[ind]
    print("Your choice: %s, Computer's choice: %s" % (player, computer))
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_lis:
        print('\033[31;1mYou Win!!!\033[0m')
        Win += 1
    else:
        print('\033[31;1mYou Lose!!!\033[0m')
        Lose += 1
    if Win > Lose:
        print('你赢了')
    else:
        print('你输了')
