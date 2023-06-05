# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/23 14:48
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : test_login.py
# @Software : PyCharm

import allure
import os
import pytest

from pageObjects.loginPage import LoginPage
from utils.handle_path import testData_path, reports_path
from utils.handle_yaml import read_yaml_data


@allure.epic('宝利商城-V2.0')  # 项目名称
@allure.feature('登录功能')  # 功能名称
class TestLogin:
    """
    测试登录功能类
    """

    @allure.story('登录业务')
    @pytest.mark.parametrize('username, password', read_yaml_data(testData_path + r'\loginData.yaml'))
    def test_login(self, username, password):
        # 执行登录操作进入主页面
        mainPage = LoginPage().to_login_page().login(username, password)
        # 断言主页面是否存在[今日下单]元素
        # assert mainPage.element_is_presence(mainPage.today_orders,action="今日下单元素")
        pytest.assume(mainPage.element_is_presence(mainPage.today_orders, action="今日下单元素"))
        mainPage.to_login_page(action="回退登录界面")


if __name__ == '__main__':
    pytest.main(['test_login.py', '-s', '--alluredir', reports_path, '--clean-alluredir'])
    os.system(f'allure serve {reports_path}')
