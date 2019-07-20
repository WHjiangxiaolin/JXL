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

#查询
# query_dep = 'SELECT * FROM departments'
# cursor.execute(query_dep)
# result1 = cursor.fetchone()   #取一行
# print(result1)
# print('*' * 40)
# result2 = cursor.fetchmany(2)  #指定取出几行,从第二行开始取
# print(result2)
# print('*' * 40)
# result3 = cursor.fetchall()   #取出全部,剩下的全部
# print(result3)
##########################################################
#移动游标
query_dep = 'SELECT * FROM departments'
cursor.execute(query_dep)
cursor.scroll(3, mode='absolute')      #必须从开头算起,进行游标移动
result = cursor.fetchone()
print(result)
print()
cursor.scroll(1)            #默认以相对当前位置移动
result2 = cursor.fetchone()
print(result2)

# 关闭游标和连接
cursor.close()
conn.close()