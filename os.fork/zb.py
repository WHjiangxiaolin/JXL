import time
import os

print('starting...')
retval = os.fork()
if retval:
    print('父进程')
    time.sleep(60)
else:
    print('子进程')
    time.sleep(20)
    exit()

print('done')

#watch -n1 ps a   终端运行命令每一秒查看进程状态