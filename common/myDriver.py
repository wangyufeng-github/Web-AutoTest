# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/18 11:16
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : myDriver.py
# @Software : PyCharm
from selenium import webdriver

from configs.config import implicitly_wait


# 单例模式，哪个类需要使用则直接继承即可
class Single(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance


class Driver(Single):
    """
    继承单例类，则该类只创建一个实例
    """
    _driver = None  # 临时变量，用于判断驱动对象

    def get_driver(self, browser_name="chrome"):
        """
        判断是否存在驱动对象，并根据不同类型浏览器创建驱动对象
        :param browser_name:
        :return:驱动对象
        """
        # 若驱动对象不存在
        if self._driver is None:
            if browser_name == "chrome":
                self._driver = webdriver.Chrome()
            elif browser_name == "firefox":
                self._driver = webdriver.Firefox()
            else:
                raise (f'没有当前{browser_name}类型的浏览器')
            # 根据配置文件设置的时间进行隐式等待
            self._driver.implicitly_wait(implicitly_wait)
            # 最大化窗口
            self._driver.maximize_window()
        return self._driver


if __name__ == '__main__':
    Driver().get_driver()
