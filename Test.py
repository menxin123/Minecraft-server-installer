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


main_menu = Menu("主菜单", ["子菜单 1", "子菜单 2", "退出"])

submenu1 = SubMenu("子菜单 1", ["选项 1", "选项 2", "返回"], main_menu)
submenu2 = SubMenu("子菜单 2", ["选项 3", "选项 4", "返回"], main_menu)

submenu1_1 = SubMenu("子菜单 1.1", ["选项 1.1", "选项 1.2", "返回"], submenu1)
submenu1_2 = SubMenu("子菜单 1.2", ["选项 1.3", "选项 1.4", "返回"], submenu1)

submenu2_1 = SubMenu("子菜单 2.1", ["选项 2.1", "选项 2.2", "返回"], submenu2)
submenu2_2 = SubMenu("子菜单 2.2", ["选项 2.3", "选项 2.4", "返回"], submenu2)

submenu1_1_1 = SubMenu("子菜单 1.1.1", ["选项 1.1.1", "选项 1.1.2", "返回"], submenu1_1)
submenu1_1_2 = SubMenu("子菜单 1.1.2", ["选项 1.1.3", "选项 1.1.4", "返回"], submenu1_1)

submenu2_1_1 = SubMenu("子菜单 2.1.1", ["选项 2.1.1", "选项 2.1.2", "返回"], submenu2_1)
submenu2_1_2 = SubMenu("子菜单 2.1.2", ["选项 2.1.3", "选项 2.1.4", "返回"], submenu2_1)

main_menu.select_option(0)

while True:
    main_menu.display()
    choice = int(input("请输入你的选择（输入0退出）："))
    if choice == 0:
        break
    main_menu.select_option(choice)

    if choice == 1:
        submenu1.display()
        sub_choice = int(input("请输入你的选择（输入0返回）："))
        if sub_choice == 0:
            continue
        submenu1.select_option(sub_choice)

        if sub_choice == 1:
            submenu1_1.display()
            sub_sub_choice = int(input("请输入你的选择（输入0返回）："))
            if sub_sub_choice == 0:
                continue
            submenu1_1.select_option(sub_sub_choice)

            if sub_sub_choice == 1:
                submenu1_1_1.display()
                sub_sub_sub_choice = int(input("请输入你的选择（输入0返回）："))
                submenu1_1_1.select_option(sub_sub_sub_choice)
            elif sub_sub_choice == 2:
                submenu1_1_2.display()
                sub_sub_sub_choice = int(input("请输入你的选择（输入0返回）："))
                submenu1_1_2.select_option(sub_sub_sub_choice)

        elif sub_choice == 2:
            submenu1_2.display()
            sub_sub_choice = int(input("请输入你的选择（输入0返回）："))
            submenu1_2.select_option(sub_sub_choice)

    elif choice == 2:
        submenu2.display()
        sub_choice = int(input("请输入你的选择（输入0返回）："))
        if sub_choice == 0:
            continue
        submenu2.select_option(sub_choice)

        if sub_choice == 1:
            submenu2_1.display()
            sub_sub_choice = int(input("请输入你的选择（输入0返回）："))
            if sub_sub_choice == 0:
                continue
            submenu2_1.select_option(sub_sub_choice)

            if sub_sub_choice == 1:
                submenu2_1_1.display()
                sub_sub_sub_choice = int(input("请输入你的选择（输入0返回）："))
                submenu2_1_1.select_option(sub_sub_sub_choice)
            elif sub_sub_choice == 2:
                submenu2_1_2.display()
                sub_sub_sub_choice = int(input("请输入你的选择（输入0返回）："))
                submenu2_1_2.select_option(sub_sub_sub_choice)

        elif sub_choice == 2:
            submenu2_2.display()
            sub_sub_choice = int(input("请输入你的选择（输入0返回）："))
            submenu2_2.select_option(sub_sub_choice)
