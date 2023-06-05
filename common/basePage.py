# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/18 11:16
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : basePage.py
# @Software : PyCharm

import os
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common.myDriver import Driver
from utils.handle_log import log
from utils.handle_path import screenshot_path, config_path
from utils.handle_yaml import read_yaml_data


class BasePage(object):
    """
    基础页面操作类，例如文本框输入、鼠标点击操作、获取元素属性、判断元素是否可见等
    """

    def __init__(self):
        # 获取驱动对象
        self._driver = Driver().get_driver()
        # 获取yaml文件中每一组Page下的元素定位方法
        locators = read_yaml_data(config_path + r'\locators.yaml')[self.__class__.__name__]
        # print(locators)
        for k, v in locators.items():  # k页面元素名称，v定位方法和表达式
            # 为页面类增加属性self.k = v
            setattr(self, k, v)

    def get_page_screenshot(self, action=None):
        """
        截取全屏
        :param action:表示执行动作
        :return:
        """
        curTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
        # 图片名称为动作+时间
        filePath = os.path.join(screenshot_path, f'{action}_{curTime}.png')
        self._driver.save_screenshot(filePath)

    def element_is_visibility(self, locator, action=None, timeout=10, poll_frequency=0.5):
        """
        判断元素是否可见
        :param locator:元素定位
        :param action: 执行动作
        :param timeout: 超时时间
        :param poll_frequency: 轮询时间
        :return:
        """
        try:
            # 显示等待元素是否可见
            element = WebDriverWait(
                driver=self._driver,
                timeout=timeout,
                poll_frequency=poll_frequency).until(
                # 元素是否可见
                EC.visibility_of_element_located(locator))
        except:
            # 截图
            self.get_page_screenshot(f'{action}-元素定位失败')
            # 记录日志
            log.info(f'元素:{locator}超出等待时间内不可见')
            raise  # 抛出异常
        return element

    def element_is_click(self, locator, action=None, timeout=10, poll_frequency=0.5):
        """
        元素是否可点击
        :param locator:
        :param action:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        try:
            element = WebDriverWait(
                driver=self._driver,
                timeout=timeout,
                poll_frequency=poll_frequency).until(
                # 判断元素是否可点击
                EC.element_to_be_clickable(locator))
        except:
            # 截图
            self.get_page_screenshot(f'{action}-元素定位失败')
            # 记录日志
            log.info(f'元素:{locator}超出等待时间内不可见')
            raise  # 抛出异常
        return element

    def input_text(self, locator, text, action=None):
        """
        文本输入
        :param locator:
        :param text:
        :param action:
        :return:
        """
        # 解包的方式传入定位参数
        element = self._driver.find_element(*locator)
        # 清空输入框
        element.clear()
        element.send_keys(text)

    def click(self, locator, action=None):
        """
        元素点击操作
        :param locator:
        :param action:
        :return:
        """
        element = self._driver.find_element(*locator)
        element.click()

    def element_is_presence(self, locator, action=None, timeout=10, poll_frequency=0.5):
        """
        判断元素是否存在
        :param locator:
        :param action:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        try:
            WebDriverWait(
                driver=self._driver,
                timeout=timeout,
                poll_frequency=poll_frequency).until(
                EC.presence_of_element_located(locator))
        except:
            self.get_page_screenshot(f'{action}-元素不存在')
            log.info(f'{locator}:元素不存在')
            return False
        return True

    def get_text(self, locator, action=None, many=False):
        """
        获取控件文本信息
        """
        if many == False:
            return self._driver.find_element(*locator).text
        elif many == True:
            eles = self._driver.find_elements(*locator)
            return [ele.text for ele in eles]


if __name__ == '__main__':
    BasePage()
