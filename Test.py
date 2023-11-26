import os


def clear_screen():
    # 判断操作系统类型
    if os.name == 'posix':  # Unix/Linux/MacOS/BSD等
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')
    else:
        # 无法识别的操作系统类型
        print("无法清屏：不支持的操作系统")


class Menu:
    def __init__(self, title, options):
        self.title = title
        self.options = options

    def display(self):
        print(self.title)
        for index, option in enumerate(self.options):
            print(f"{index + 1}. {option}")

    def select_option(self, choice):
        pass


class SubMenu(Menu):
    def __init__(self, title, options, parent_menu):
        super().__init__(title, options)
        self.parent_menu = parent_menu

    def select_option(self, choice):
        if choice == 0:
            return
        selected_option = self.options[choice - 1]
        print(f"You selected: {selected_option}")
        # 在这里添加你希望执行的逻辑


text = "请输入你的选择（输入t退出）："

main_menu = Menu("---------主菜单---------", ["minecraft server", "forge server", "fabric server","cat server","mo server","bukkit server","spigot server","paper server"])

core_choice1 = SubMenu("子菜单 1", ["选项 1", "选项 2", "返回"], main_menu)
core_choice2 = SubMenu("子菜单 2", ["选项 3", "选项 4", "返回"], main_menu)

submenu1_1 = SubMenu("子菜单 1.1", ["选项 1.1", "选项 1.2", "返回"], core_choice1)
submenu1_2 = SubMenu("子菜单 1.2", ["选项 1.3", "选项 1.4", "返回"], core_choice1)

submenu2_1 = SubMenu("子菜单 2.1", ["选项 2.1", "选项 2.2", "返回"], core_choice2)
submenu2_2 = SubMenu("子菜单 2.2", ["选项 2.3", "选项 2.4", "返回"], core_choice2)

submenu1_1_1 = SubMenu("子菜单 1.1.1", ["选项 1.1.1", "选项 1.1.2", "返回"], submenu1_1)
submenu1_1_2 = SubMenu("子菜单 1.1.2", ["选项 1.1.3", "选项 1.1.4", "返回"], submenu1_1)

submenu2_1_1 = SubMenu("子菜单 2.1.1", ["选项 2.1.1", "选项 2.1.2", "返回"], submenu2_1)
submenu2_1_2 = SubMenu("子菜单 2.1.2", ["选项 2.1.3", "选项 2.1.4", "返回"], submenu2_1)

main_menu.select_option(0)

while True:
    main_menu.display()
    choice = int(input(text))
    if choice == 0:
        exit()

    if choice == 1:
        clear_screen()
        core_choice1.display()
        sub_choice = int(input("请输入你的选择（输入t返回）："))
        if sub_choice == 0:
            exit()

        if sub_choice == 1:
            clear_screen()
            submenu1_1.display()
            sub_sub_choice = int(input("请输入你的选择（输入0返回）："))
            if sub_sub_choice == 0:
                exit()

            if sub_sub_choice == 1:
                clear_screen()
                submenu1_1_1.display()
                sub_sub_sub_choice = int(input("请输入你的选择（输入0返回）："))
            elif sub_sub_choice == 2:
                clear_screen()
                submenu1_1_2.display()
                sub_sub_sub_choice = int(input("请输入你的选择（输入0返回）："))

        elif sub_choice == 2:
            clear_screen()
            submenu1_2.display()
            sub_sub_choice = int(input("请输入你的选择（输入0返回）："))


    elif choice == 2:
        clear_screen()
        core_choice2.display()
        sub_choice = int(input("请输入你的选择（输入tt返回）："))
        if sub_choice == 0:
            exit()

        if sub_choice == 1:
            clear_screen()
            submenu2_1.display()
            sub_sub_choice = int(input("请输入你的选择（输入0返回）："))
            if sub_sub_choice == 0:
                exit()

            if sub_sub_choice == 1:
                clear_screen()
                submenu2_1_1.display()
                sub_sub_sub_choice = int(input("请输入你的选择（输入0返回）："))
            elif sub_sub_choice == 2:
                clear_screen()
                submenu2_1_2.display()
                sub_sub_sub_choice = int(input("请输入你的选择（输入0返回）："))

        elif sub_choice == 2:
            clear_screen()
            submenu2_2.display()
            sub_sub_choice = int(input("请输入你的选择（输入0返回）："))

            submenu2_2.select_option(sub_sub_choice)
