import random
                #用户猜对数字,不再显示答案,4次全错,才显示答案
num = random.randint(1,10)
counter = 0

while counter < 4:  #只允许猜4次
    answer = int(input('请输入1-10的数字: '))
    if answer > num:
        print('你猜大了')
    elif answer < num:
        print('你猜小了')
    else:
        print('你猜对了')
        break
    counter += 1

else:   #只在循环结束后执行,如果循环被break,else就不执行,否则执行
    print('answer is: %s' % num)
