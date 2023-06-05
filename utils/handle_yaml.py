# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/18 15:38
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : handle_yaml.py
# @Software : PyCharm

import yaml


def read_yaml_data(fileDir):
    """
    读取yaml文件内容
    :param fileDir:
    :return:
    """
    with open(fileDir, encoding='utf-8') as file:
        return yaml.safe_load(file.read())


if __name__ == '__main__':
    res = read_yaml_data(r'../data/loginData.yaml')
    print(res)
