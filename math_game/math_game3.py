#100以内数字加减法练习

from random import randint,choice

def exam():
    cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)
    op = choice('+-')
    #计算出正确答案
    result = cmds[op](*nums)

    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    counter = 0
    while counter < 3:
        try:
            answer = int(input(prompt))
        except:
            print()
            continue

        if answer == result:
            print('你真棒!!!')
            break
        print('不对哟')
        counter += 1
    else:
        print('The Anser is: %s%s' % (prompt, result))

def main():
    while True:
        exam()
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        except ImportError:
            yn = 'y'
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
