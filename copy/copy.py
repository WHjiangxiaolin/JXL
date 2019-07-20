#制作copy模块

import sys
#src_fname = '/bin/ls'
#dst_fname = '/tmp/list6'

def copy(src_fname, dst_fname):
    src_fobj = open(src_fname, 'rb')  #以读方式打开源文件
    dst_fobj = open(dst_fname, 'wb')  #以写方式打开目标文件

    while True:
        data = src_fobj.read(4096)   #防止目标文件过大,每次读取4096字节
        if not data:			#读取源文件数据,数据没有时退出循环
            break
        dst_fobj.write(data)         #将数据写入目标文件

    src_fobj.close()                 #关闭源文件
    dst_fobj.close()			#关闭目标文件



copy(sys.argv[1], sys.argv[2])   #传参,读取命令行下的参数
