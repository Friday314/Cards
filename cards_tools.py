def show_menu():

    """欢迎界面"""

    print("*****" * 10)
    print("欢迎「使用名片管理系统」V1.0\n")
    print("1、新建名片")
    print("2、显示全部")
    print("3、查询名片\n")
    print("0、退出系统")
    print("*****" * 10)


# 定义一个列表，用作存放名片
card_list = []


def new_card():

    """新增名片"""

    print("-----" * 10)

    # 1、提示用户输入名片详细信息
    set_str_name = input("请输入姓名：")
    set_str_phone = input("请输入电话:")
    set_str_qq = input("请输入QQ号码:")
    set_str_email = input("请输入邮箱:")

    # 2、使用用户输入的信息建立一个名片字典
    card_dict = {"Name": set_str_name,
                 "Phone": set_str_phone,
                 "QQ": set_str_qq,
                 "Email": set_str_email}

    # 3、将名片字典添加到列表中
    card_list.append(card_dict)
    # print(card_list)
    print('名片"%s"添加成功' % set_str_name)


def show_all():

    """显示所有名片"""

    print("-----" * 10)

    # 判断名片列表中是否有值
    if len(card_list) != 0:

        # 打印表头
        print("姓名\t\t电话\t\tQQ\t\t邮箱")
        print("-----" * 10)

        # 遍历列表字典
        for card_dict in card_list:
                print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["Name"],
                                                card_dict["Phone"],
                                                card_dict["QQ"],
                                                card_dict["Email"]))
    else:
        print("名片管理为空！请加名片！")


def search_card():

    """搜索名片"""

    print("-----" * 10)
    # 1、提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名：")

    # 2、遍历名片字典，查询要索搜的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:
        if find_name in card_dict["Name"]:

            # 打印表头
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("-----" * 10)

            # 打印名片信息
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["Name"],
                                            card_dict["Phone"],
                                            card_dict["QQ"],
                                            card_dict["Email"]))
            # 选择名片相关操作
            update_card(card_dict)
            break
    else:
        print("抱歉，未找到%s的名片信息" % find_name)


def update_card(card_dict):

    """处理查找到的名片

    :rtype: object
    """
    # print(card_dict)

    number = int(input("请选择要执行的操作「1、修改  2、删除  0、返回」："))

    if number == 1:

        """
        优化代码
        
        update_name = input("请输入姓名「回车不修改」：")

        # 判断非空
        if update_name != "":
            card_dict["Name"] = update_name

        update_phone = input("请输入电话「回车不修改」：")

        # 判断非空
        if update_phone != "":
            card_dict["Phone"] = update_phone

        update_qq = input("请输入QQ「回车不修改」：")

        # 判断非空
        if update_qq != "":
            card_dict["QQ"] = update_qq

        update_email = input("请输入Email「回车不修改」：")

        # 判断非空
        if update_email != "":
            card_dict["Email"] = update_email
        
        """

        # 优化代码，判断用户输入为空

        card_dict["Name"] = input_card_info(card_dict["Name"], "请输入姓名「回车不修改」：")
        card_dict["Phone"] = input_card_info(card_dict["Phone"], "请输入电话「回车不修改」：")
        card_dict["QQ"] = input_card_info(card_dict["QQ"], "请输入QQ「回车不修改」：")
        card_dict["Email"] = input_card_info(card_dict["Email"], "请输入Email「回车不修改」：")

        print("用户%s修改成功！" % card_dict["Name"])

    elif number == 2:

        # 删除名片
        card_list.remove(card_dict)
        print("名片删除成功！")

    elif number == 0:

        return

    else:
        print("输入错误，请重新输入")
        search_card()


def input_card_info(dict_value, tip_message):

    """输入名片信息

    :param dict_value:字典中原有的数据
    :param tip_message:输入提示文字
    :return:如果用户输入了内容，就返回内容，否则返回字典中原有的值
    """
    # 1、提示用户输入内容
    result_str = input(tip_message)

    # 2、针对用户的输入进行判断，如果用户输入了结果，直接返回结果
    if len(result_str) > 0:

        return result_str

    # 3、如果用户没有输入，返回"字典中原有数据"
    else:
        return dict_value
