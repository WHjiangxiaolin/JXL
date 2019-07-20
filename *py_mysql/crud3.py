from dbconn import Employees, Departments, Salary, Session

# 创建会话实例，用于连接数据库
session = Session()

# 创建员工实例
gz1 = Salary(
    id = 1,
    date = '2019-06-10',
    emp_id = 1,
    basic = 8000,
    awards = 2000,
)
gz2 = Salary(
    id = 2,
    date = '2019-06-10',
    emp_id = 2,
    basic = 8000,
    awards = 2000,
)
gz3 = Salary(
    id = 3,
    date = '2019-06-10',
    emp_id = 3,
    basic = 8000,
    awards = 1555,
)
gz4 = Salary(
    id = 4,
    date = '2019-06-10',
    emp_id = 4,
    basic = 8000,
    awards = 1666,
)
gz5 = Salary(
    id = 5,
    date = '2019-06-10',
    emp_id = 5,
    basic = 8500,
    awards = 1600,
)
gz6 = Salary(
    id = 6,
    date = '2019-06-10',
    emp_id = 6,
    basic = 8500,
    awards = 1500,
)
gz7 = Salary(
    id = 7,
    date = '2019-06-10',
    emp_id = 7,
    basic = 8500,
    awards = 1500,
)
gz8 = Salary(
    id = 8,
    date = '2019-06-10',
    emp_id = 8,
    basic = 8500,
    awards = 1800,
)
gz9 = Salary(
    id = 9,
    date = '2019-06-10',
    emp_id = 9,
    basic = 9000,
    awards = 1800,
)
gz10 = Salary(
    id = 10,
    date = '2019-07-10',
    emp_id = 1,
    basic = 8500,
    awards = 1500,
)
gz11 = Salary(
    id = 11,
    date = '2019-07-10',
    emp_id = 2,
    basic = 8500,
    awards = 2222,
)
gz12 = Salary(
    id = 12,
    date = '2019-07-10',
    emp_id = 3,
    basic = 8500,
    awards = 2222,
)
gz13 = Salary(
    id = 13,
    date = '2019-07-10',
    emp_id = 4,
    basic = 10000,
    awards = 2000,
)
gz14 = Salary(
    id = 14,
    date = '2019-07-10',
    emp_id = 5,
    basic = 10000,
    awards = 2000,
)
gz15 = Salary(
    id = 15,
    date = '2019-07-10',
    emp_id = 6,
    basic = 10000,
    awards = 2500,
)
gz16 = Salary(
    id = 16,
    date = '2019-07-10',
    emp_id = 7,
    basic = 9500,
    awards = 2500,
)
gz17 = Salary(
    id = 17,
    date = '2019-07-10',
    emp_id = 8,
    basic = 9500,
    awards = 2500,
)
gz18 = Salary(
    id = 18,
    date = '2019-07-10',
    emp_id = 9,
    basic = 9500,
    awards = 3000,
)

# 在数据库中创建记录
emps = [gz1, gz2, gz3, gz4, gz5, gz6, gz7, gz8, gz9, gz10, gz11, gz12, gz13, gz14,
        gz15, gz16, gz17, gz18]
session.add_all(emps)
session.commit()    # 确认至数据库

session.close()