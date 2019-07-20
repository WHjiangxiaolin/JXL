from datetime import datetime

logfole = 'web_log'
t9 = datetime(2019, 5, 15, 9)
t12 = datetime(2019, 5, 15, 12)

with open(logfole) as fobj:
    for line in fobj:
        t = datetime.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        if t > t12:
            break
        if t >= t9:
            print(line, end='')