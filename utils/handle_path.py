# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/18 14:57
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : handle_path.py
# @Software : PyCharm
import os

# 当前工程路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 截图路径
screenshot_path = os.path.join(project_path, r'outFiles\screenshot')
# 日志路径
logs_path = os.path.join(project_path, r'outFiles\logs')
# 测试数据路径
testData_path = os.path.join(project_path, r'data')
# 测试报告路径
reports_path = os.path.join(project_path, r'outFiles\reports\tmp')
# 配置路径
config_path = os.path.join(project_path, r'configs')

if __name__ == '__main__':
    print(reports_path)
    print(project_path)
    print(testData_path)
