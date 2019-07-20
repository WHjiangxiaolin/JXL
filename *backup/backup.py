#-将/tmp/demo/security备份到/tmp/demo/backup中
#- 需要支持完全和增量备份
#- 周一执行完全备份
#- 其他时间执行增量备份

#分析：
#- 完全备份需要执行备份目录、计算每个文件的md5值
#- 增量备份需要计算文件的md5值，把md5值与前一天的md5值比较，有变化的文件要备份；目录中新增的文件也要备份
#- 备份的文件名，应该体现出：备份的是哪个目录，是增量还是完全，哪一天备份的

import tarfile
from time import strftime
import os
import hashlib
import pickle

def check_md5(fname):    #生成文件MD5值,该函数下面给下面函数用
    m = hashlib.md5()

    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()

def full_backup(src, dst, md5file):  #完全备份
    # 将完全备份文件名组合起来,os.path.basename(src)可以取目录最后的目录名
    fname = '%s_full_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)    #将完全备份文件绝对路径组合起来

    tar = tarfile.open(fname, 'w:gz')	#打包备份文件
    tar.add(src)
    tar.close()

    # 计算每个文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
	#os.walk返回值由多个元祖构成,每个元祖有三项,第一项时路径字符串,第二项是该路径下的目录列表,第三项时该目录下的文件列表.path, folders, files对应此三项,由path和file组合成文件绝对路径
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)    #生成文件MD5值,并保存为字典的值,字典的键为文件名

    # 把md5值字典保存到文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

def incr_backup(src, dst, md5file):    #增量备份
    #将增量备份文件名组合起来
    fname = '%s_incr_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)   #将增量备份文件绝对路径组合起来

    # 取出前一天的文件md5值
    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)

    # 计算当前下文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)      #生成文件MD5值,并保存为字典的值,字典的键为文件名

    # 找出变化的文件和新增的文件，把它们压缩
    tar = tarfile.open(fname, 'w:gz')
    for key in md5dict:
        # get  如果key不在字典中返回None则表示判断不成立,则之前的目录中没有这个文件
        if old_md5.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()

    # 把当前的md5字典写到文件中，以便下一次比较使用
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/demo/backup'
    md5file = '/tmp/demo/backup/md5.data'
    if strftime('%a') == 'Mon':   #星期几时%a
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)
