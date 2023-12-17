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