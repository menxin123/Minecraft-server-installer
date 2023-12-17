
def function1(item):
    print(f"执行函数1，选项内容：{item}")

def function2(item):
    print(f"执行函数2，选项内容：{item}")

def function3(item):
    print(f"执行函数3，选项内容：{item}")

# 定义一个字典，将选项索引映射到相应的函数
函数映射 = {
    0: function1,
    1: function2,
    2: function3
}

def display_menu(list_name):
    content_list = list_name
    items_per_page = 3
    current_page = 0
    max_page_num = len(content_list) // items_per_page + 1

    while True:
        print("当前页内容：")
        start_index = current_page * items_per_page
        end_index = (current_page + 1) * items_per_page
        for i in range(start_index, min(end_index, len(content_list))):
            print(f"{i+1}. {content_list[i]}")

        user_input = input("输入a切换上一页，输入b切换下一页，输入q退出，选择内容编号执行自定义函数：")
        if user_input == 'a':
            current_page -= 1
            if current_page < 0:
                current_page = max_page_num - 1
        elif user_input == 'b':
            current_page += 1
            if current_page >= max_page_num:
                current_page = 0
        elif user_input == 'q':
            break
        else:
            try:
                selected_item_index = int(user_input) - 1
                if start_index <= selected_item_index < end_index and selected_item_index in 函数映射:
                    selected_item = content_list[selected_item_index]
                    函数映射[selected_item_index](selected_item)  # 调用相应的函数，并传递选项内容
                else:
                    print("无效的选择，请重新输入。")
            except ValueError:
                print("无效的选择，请重新输入。")

# 主菜单
def main_menu():
    list1 = [
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

    list2 = [
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

    while True:
        print("请选择要使用的列表：")
        print("1. 列表1")
        print("2. 列表2")
        print("3. 退出")

        user_input = input("请输入选项：")
        if user_input == '1':
            display_menu(list1)
        elif user_input == '2':
            display_menu(list2)
        elif user_input == '3':
            break
        else:
            print("无效的选择，请重新输入。")

# 运行主菜单
main_menu()
