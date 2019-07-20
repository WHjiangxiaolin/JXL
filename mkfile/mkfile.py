#创建文件

import os

def get_fname():
    while True:
        fname = input('filename: ')     #输入要创建的文件名
        if not os.path.exists(fname):
            break					#判断文件是否存在,如果存在就退出
        print('文件已存在,请重输入.')

    return fname

def get_cotent():
    content = []

    print('请输入内容,输入end表示结束')     #输入向写入文件的内容,输入end结束
    while True:
        line = input('(end to quit)> ')
        if line == 'end':
            break
        content.append(line)     #将输入内容添加到列表

    return content

def wfile(fname, content):
    with open(fname, 'w') as fobj:    #将列表数据每一行读取处理写入到文件
        fobj.writelines(content)

if __name__ == '__main__':
    fname = get_fname()
    content = get_cotent()
    content = ['%s\n' % line for line in content]   #为了看到换行效果加\n
    wfile(fname, content)
