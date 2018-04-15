import cards_tools


def main():

    while True:
        # 显示功能菜单
        cards_tools.show_menu()

        number = int(input("请选择希望执行的操作："))

        if number == 1:

            print("您选择的操作是「新建名片」")
            cards_tools.new_card()

        elif number == 2:

            print("您选择的操作是「显示全部」")
            cards_tools.show_all()

        elif number == 3:

            print("您选择的操作是「查询名片」")
            cards_tools.search_card()

        elif number == 0:

            print("程序退出！谢谢使用！")
            break

        else:
            print("输入错误，请重新输入！")


main()
