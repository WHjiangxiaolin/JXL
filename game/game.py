#石头/剪刀/布 游戏

import random
cq = input('你的出拳(石头|剪刀|布): ')
jq = random.choice(['石头', '剪刀', '布'])
print('电脑出的是:'+jq)

if cq == '石头':
    if cq == jq:
        print('平局')
    elif jq == '剪刀':
        print('你赢了')
    else:
        print('你输了')
elif cq == '剪刀':
    if cq == jq:
        print('平局')
    elif jq == '布':
        print('你赢了')
    else:
        print('你输了')
elif cq == '布':
    if cq == jq:
        print('平局')
    elif jq == '石头':
        print('你赢了')
    else:
        print('你输了')
else:
    print('只能输入石头|剪刀|布')
