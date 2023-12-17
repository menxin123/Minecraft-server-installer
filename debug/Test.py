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


text = '-'*23 + "\n请输入你的选择（输入t退出）："

main_menu = Menu("---------主菜单---------", ["minecraft server", "forge server", "fabric server","cat server","mo server","bukkit server","spigot server","paper server"])

core_choice1 = SubMenu("minecrafr server", sorted(["1.20.2", "1.20.1", "1.20", "1.19.4", "1.19.3", "1.19.2", "1.19.1", "1.19", "1.18.2", "1.18.1", "1.18", "1.17.1", "1.17", "1.16.5", "1.16.4", "1.16.3", "1.16.2", "1.16.1", "1.16", "1.15.2", "1.15.1", "1.15", "1.14.4", "1.14.3", "1.14.2", "1.14.1", "1.14", "1.13.2", "1.13.1", "1.13", "1.12.2", "1.12.1", "1.12", "1.11.2", "1.11.1", "1.11", "1.10.2", "1.10.1", "1.10", "1.9.4", "1.9.3", "1.9.2", "1.9.1", "1.9", "1.8.9", "1.8.8", "1.8.7", "1.8.6", "1.8.5", "1.8.4", "1.8.3", "1.8.2", "1.8.1", "1.8", "1.7.10", "1.7.9", "1.7.8", "1.7.7", "1.7.6", "1.7.5", "1.7.4", "1.7.2", "1.6.4", "1.6.2", "1.6.1", "1.5.2", "1.5.1", "1.5", "1.4.7", "1.4.6", "1.4.5", "1.4.4", "1.4.2", "1.3.2", "1.3.1", "1.2.5", "1.2.4", "1.2.3", "1.2.2", "1.2.1", "1.1", "1.0.1", "1.0.0"]), main_menu)
core_choice2 = SubMenu("forge server", sorted(["1.20", "1.20.4", "1.20.3", "1.20.2", "1.20.1", "1.20", "1.19", "1.19.4", "1.19.3", "1.19.2", "1.19.1", "1.19", "1.18", "1.18.2", "1.18.1", "1.18", "1.17.1", "1.16.5", "1.16.4", "1.16.3", "1.16.2", "1.16.1", "1.15", "1.15.2", "1.15.1", "1.15", "1.14.4", "1.14.3", "1.14.2", "1.13.2", "1.12", "1.12.2", "1.12.1", "1.12", "1.11", "1.11.2", "1.11", "1.10", "1.10.2", "1.10", "1.9", "1.9.4", "1.9", "1.8", "1.8.9", "1.8.8", "1.8", "1.7.10", "1.7.10_pre4", "1.7.2", "1.6.4", "1.6.3", "1.6.2", "1.6.1", "1.5", "1.5.2", "1.5.1", "1.5", "1.4.7", "1.4.6", "1.4.5", "1.4.4", "1.4.3", "1.4.2", "1.4.1", "1.4.0", "1.3.2", "1.2.5", "1.2.4", "1.2.3", "1.1"]), main_menu)
core_choice3 = SubMenu("fabric server",["选项5","选项6","返回"],main_menu)
core_choice4 = SubMenu("cat server",["选项7","选项8","返回"],main_menu)
core_choice5 = SubMenu("mo server",["选项9","选项10","返回"],main_menu)
core_choice6 = SubMenu("bukkit server",["选项11","选项12","返回"],main_menu)
core_choice7 = SubMenu("spigot server",["选项12","选项13","返回"],main_menu)
core_choice8 = SubMenu("paper server",["选项14","选项15","返回"],main_menu)


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
