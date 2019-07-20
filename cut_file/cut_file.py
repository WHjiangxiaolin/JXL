# 获取web_log中，2019-05-15号9:00到12:00之间的数据
# 思路：定义出9点和12点的时间格式；再从文件中取出时间，把时间字符串、
# 也转换成时间格式。比较这个时间是不是在9到12点之间即可

import time

logfile = 'web_log'
t9 = time.strptime('2019-05-15 09:00:00', '%Y-%m-%d %H:%M:%S')
t12 = time.strptime('2019-05-15 12:00:00', '%Y-%m-%d %H:%M:%S')

with open(logfile) as fobj:
    for line in fobj:
        t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        if t > t12:
            break
        if t >= t9:
            print(line, end='')