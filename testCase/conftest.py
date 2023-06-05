# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/23 14:33
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : conftest.py
# @Software : PyCharm
import time

import pytest

from common.myDriver import Driver


# 使用pytest指定作用范围为测试会话期间只执行一次
@pytest.fixture(scope="session", autouse=True)
def start_running():
    print('---宝利商场V2--UI自动化测试开始执行！---')
    yield  # 使用改关键字阻塞，直到用例执行结束
    time.sleep(5)
    Driver().get_driver().quit()
    print('---宝利商场V2--UI自动化测试执行结束！---')
