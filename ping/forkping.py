import subprocess
import os

def ping(host):
    result = subprocess.run(
        'ping -c2 %s &> /dev/null' % host, shell=True
    )
    if result.returncode == 0:
        print('%s:up' % host)
    else:
        print('%s:down' % host)

if __name__ == '__main__':
    ips = ('176.215.111.%s' % i for i in range(1,255))
    for ip in ips:
        retval = os.fork()   #开启多个子进程
        if retval == 0:
            ping(ip)
            exit()	#子进程执行完任务后退出
