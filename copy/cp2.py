src_fname = '/bin/ls'
dst_fname = '/tmp/list4'

src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')

while True:
    data = src_fobj.read(4096)   # 每次最多读4096字节
    # if not data:
    if len(data) == 0:
    # if data == b'':   # data值为b''，表示False
        break
    dst_fobj.write(data)

src_fobj.close()
dst_fobj.close()