#创建一个记账的程序,将收入\支出进行详细的记录

import os
import pickle
from time import strftime

def save(fname):			#存钱
    date = strftime('%Y-%m-%d')   #日期
    amount = int(input('amount: '))   #存钱的金额,如果是小数可以用flody
    comment = input('comment: ')      #说明
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)   #将账单所有数据取出到列表中
    balance = records[-1][-2] + amount    #余额
    new_record = [date, amount, 0, balance, comment]   #最新的一笔收入情况写成列表
    records.append(new_record)          #将最新一笔收入追加到列表
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)      #将列表所有数据导入到账单

def cost(fname):			#支出
    date = strftime('%Y-%m-%d')
    amount = int(input('amount: '))  #支出的金额
    comment = input('comment: ')
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    balance = records[-1][-2] - amount
    new_record = [date, 0, amount, balance, comment]
    records.append(new_record)
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def query(fname):      #查询
    print('%-12s%-8s%-8s%-12s%-15s' % ('date', 'save', 'cost', 'balance', 'comment')) #打印第一列
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    for line in records: 
        print('%-12s%-8s%-8s%-12s%-15s' % tuple(line))    #打印每一项
    print()

def show_menu():
    cmds = {'0':save, '1':cost, '2':query}
    prompt = """(0) save
(1) cost
(2) query
(3) quit
Please input your choice(0/1/2/3): """
    fname = 'record.data'
    init_data = [
        ['2019-07-09', 0, 0, 10000, 'init'],
    ]
    if not os.path.exists(fname):		# 如果还没有record.data文件，则创建
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)

    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('Invalid choice, try again.')
            continue

        if choice == '3':
            print('\nBye-bye')
            break

        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()
