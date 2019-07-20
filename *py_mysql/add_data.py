import pymysql

# 建立到数据库的连接
conn = pymysql.connect(
    host='192.168.4.10',
    port=3306,
    user='jxl',
    passwd='123456',
    db='nsd1902',
    charset='utf8'
)

# 创建游标，用于将来执行SQL语句
cursor = conn.cursor()

##################################################
# 向部门表中插入数据
#1.编写SQL语句
insert_dep = 'INSERT INTO departments VALUES (%s, %s)'
# #填写每个部门的字段值
# hr = (1, '人事部')
# ops = (2, '运维部')
# dev = (3, '开发部')
# qa = (4, '测试部')
market = (5, '市场部')

# deps = [ops, dev, qa]
#
# # 执行SQL语句
# cursor.execute(insert_dep, hr)          #插入一条数据,数据必须是元祖
# cursor.executemany(insert_dep, deps)    #插入多条数据,数据必须是列表
cursor.executemany(insert_dep, [market, (6, '财务部'), (7, '销售部')])
######################################################################
#2. 删除市场部
# del_dep = 'DELETE FROM departments WHERE dep_name=%s'
# cursor.execute(del_dep, ('市场部',))
#
# #3. 修改
# update_dep = 'UPDATE departments SET dep_name=%s WHERE dep_name=%s'
# cursor.execute(update_dep, ('人力资源部', '人事部'))


# 确认
conn.commit()

# 关闭游标和连接
cursor.close()
conn.close()