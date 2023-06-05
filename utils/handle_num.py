# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/29 10:20
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : handle_num.py
# @Software : PyCharm
import random
import string


def ran_str(num):
    """
    随机生成字符串
    :param num:
    :return:
    """
    str1 = string.ascii_letters  # 分别返回26个字母的小写和大写
    # print(str1)
    str2 = string.digits  # 阿拉伯数字0-9
    # print(str2)
    salt = "".join(random.sample("%s%s" % (str1, str2), num))
    return salt


if __name__ == '__main__':
    print(ran_str(5))
