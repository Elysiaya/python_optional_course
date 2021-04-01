def mysplit(string):
    """
    分割字符串
    :param string: 字符串
    :return:
    """
    # a = [print(i.upper()) for i in string.split(' ')]

    string_list = string.split(' ')
    for i in string_list:
        i = Myupper(i)
        print(i)


def Myupper(string):
    """
    字符串转大写
    :param string:
    :return:
    """
    return string.upper()


mysplit('Luyu is a good boy')
