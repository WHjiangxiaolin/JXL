stack = []

def pop_it():
    if stack:
        print('从栈中弹出: %s' % stack.pop())
    print('空栈')

def push_it():
    stack.append(input('数据: '))

def view_it():
    print(stack)

def show_menu():
    cmds = {'0':pop_it, '1':push_it, '2':view_it}
    prompt = """(0)出栈
(1)压栈
(2)查询
(3)退出
请选择(0/1/2/3): """

    while True:
        # 删除用户输入字符串两端的空格
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('无效输出,请重试')
            continue
        if choice == '3':
            print('bye-bye')
            break

        cmds[choice]()  #从字典中取出函数并使用
        # if choice == '0':
        #     pop_it()
        # elif choice == '1':
        #     push_it()
        # elif choice == '2':
        #     view_it()
        # else:
        #     print('bye-bye')
        #     break

if __name__ == '__main__':
    show_menu()