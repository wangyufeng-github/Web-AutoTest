# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/23 14:12
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : loginPage.py
# @Software : PyCharm
import time

from common.basePage import BasePage
from configs.config import url
from pageObjects.mainPage import MainPage


class LoginPage(BasePage):
    """
    登录界面
    """

    def to_login_page(self):
        """
        进入登录界面
        :return:
        """
        self._driver.get(url)
        return self

    def login(self, username, password):
        """
        执行登录操作
        :param username:
        :param password:
        :return:
        """
        self.input_text(self.username_input, username, action="账号输入操作")
        time.sleep(2)
        self.input_text(self.pwd_input, password, action="密码输入操作")
        time.sleep(2)
        self.click(self.login_btn, action="点击登录操作")
        time.sleep(2)
        return MainPage()


if __name__ == '__main__':
    mainpage = LoginPage().to_login_page().login("松勤老师", "123456")
    mainpage.to_productlist_page()
