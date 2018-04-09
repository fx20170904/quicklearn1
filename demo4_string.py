# -*- coding:utf-8 -*-

__author__ = 'kuyezi'

if __name__ == "__main__":
    source_str = u"it's my book, please show it, wa ka ka, yo yo yo!"

    # 从左向右查找yo
    print(u'从左向右查找yo')
    print(source_str.find("o"))
    print(source_str.index("t"))

    # 从右向左查找yo
    print(u'从右向左查找yo')
    print(source_str.find('o'))
    print(source_str.rindex('t'))

    # 替换所以的yo
    des_str = source_str.replace("yo", "ha")
    print(des_str)

    # 替换两次yo
    des_str = source_str.replace("yo", "ha", 2)
    print(des_str)