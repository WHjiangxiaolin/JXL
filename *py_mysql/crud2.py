from dbconn import Departments, Employees, Salary, Session

session = Session()

mxz = Employees(
    emp_id = 1,
    emp_name = '孟宪峥',
    birth_date = '1994-05-12',
    email = 'mxz@163.com',
    dep_id = 2
)
wj = Employees(
    emp_id = 2,
    emp_name = '翁俊',
    birth_date = '1996-03-21',
    email = 'wj@qq.com',
    dep_id = 2,
)
xzc = Employees(
    emp_id = 3,
    emp_name = '向子辰',
    birth_date = '1995-08-09',
    email = 'xzc@qq.com',
    dep_id = 3
)
llc = Employees(
    emp_id = 4,
    emp_name = '李良辰',
    birth_date = '1995-04-25',
    email = 'llc@163.com',
    dep_id = 1
)
yty = Employees(
    emp_id = 5,
    emp_name = '岳天宇',
    birth_date = '1992-11-23',
    email = 'yty@qq.com',
    dep_id = 4
)
wxm = Employees(
    emp_id = 6,
    emp_name = '王续敏',
    birth_date = '1995--6-15',
    email = 'wxm@163.com',
    dep_id = 5
)
lt = Employees(
    emp_id = 7,
    emp_name = '刘涛',
    birth_date = '1989-05-18',
    email = 'lt@tedu.com',
    dep_id = 3
)
wy = Employees(
    emp_id = 8,
    emp_name = '汪洋',
    birth_date = '1994-12-11',
    email = 'wy@163.com',
    dep_id = 6
)
mzy = Employees(
    emp_id = 9,
    emp_name = '莫振宇',
    birth_date = '1991-11-11',
    email = 'mzy@qq.com',
    dep_id = 7
)

emps = [mxz, wj, xzc, llc, yty, wxm, lt, wy, mzy]
session.add_all(emps)
session.commit()

session.close()