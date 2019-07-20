try:
    num = int(input('number: '))
    result = 100 / num

except (ValueError,ZeroDivisionError) as e:
    #将系统原本的报错信息保存到变量e中
    print('无效的输出:', e)
except (KeyboardInterrupt,EOFError):
    print('\nbye-bye')
    exit(1)
else:
    print(result)    #错误语句不执行时才输出
finally:
    print('Done')    #不管错误语句是否执行时都输出

print('正常结束')