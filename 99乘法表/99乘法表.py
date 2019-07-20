#打印99乘法表

for i in range(9,0,-1):
    for n in range(9,i-1,-1):
        c = i * n
        print('%s * %s = %s' % (i,n,c), end = ' ')    #end表示本次循环打印到一行
    print()    #打印空白换行
