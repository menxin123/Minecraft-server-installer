

# 示例选项列表1和函数映射1
content_list1 = [
    '内容1',
    '内容2',
    '内容3',
    '内容4',
    '内容5',
    '内容6',
    '内容7',
    '内容8',
    '内容9'
]

def function1():
    print("执行函数1a")

def function2():
    print("执行函数2b")

def function3():
    print("执行函数3c")

item_functions1 = {
    0: function1,
    1: function2,
    2: function3
}

# 示例选项列表2和函数映射2
content_list2 = [
    '选项1',
    '选项2',
    '选项3',
    '选项4',
    '选项5',
    '选项6',
    '选项7',
    '选项8',
    '选项9'
]

def function4():
    print("执行函数4d")

def function5():
    print("执行函数5e")

def function6():
    print("执行函数6f")

item_functions2 = {
    0: function4,
    1: function5,
    2: function6
}

# 主菜单选项
def main_menu():
    while True:
        user_input = input("请选择要使用的选项列表：\n1. 选项列表1\n2. 选项列表2\n输入q退出\n")
        if user_input == '1':
            execute_option_logic(content_list1, item_functions1)
        elif user_input == '2':
            execute_option_logic(content_list2, item_functions2)
        elif user_input == 'q':
            break
        else:
            print("无效的选择，请重新输入。")

# 调用主菜单函数
main_menu()
