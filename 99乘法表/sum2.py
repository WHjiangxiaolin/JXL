sum = 0
counter = 0
                #计算1到100之间偶数的和
while counter < 100:
    counter += 1

    if counter % 2 == 1:
    #if counter % 2:    #这种方法也可以,余数只能是1或0,1为True执行下面一条命令,0为Flas
        continue     #跳出此次循环,不管后面的命令,进行下一次循环

    sum += counter     #循环内的命令,每次循环后执行

print(sum)