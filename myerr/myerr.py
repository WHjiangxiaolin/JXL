try:
    num = int(input('number: '))
    result = 100 / num
    print(result)
    print('Done')

except ValueError:
    print('无效的输出')
except ZeroDivisionError:
    print('无效的输出')
except KeyboardInterrupt:
    print('\nbye-bye')
except EOFError:
    print('\nbye-bye')
