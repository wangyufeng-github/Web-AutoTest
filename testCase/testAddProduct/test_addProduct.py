# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/24 13:42
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : test_addProduct.py
# @Software : PyCharm
import allure
import os
import pytest
import time

from utils.handle_num import ran_str
from utils.handle_path import reports_path

"""
添加商品测试思路：
1-调用fixture登录到主页面，并返回mainpage页面对象
2-从登录界面到添加商品页面
3-进行商品添加
4-到商品列表界面判断商品是否添加成功
"""


@allure.epic('宝利商城-V2.0')
@allure.feature('商品管理')
class TestAddProduct:
    @allure.story('添加商品页面')
    def test_add_product(self, init_page):  # fixture通过参数形式传递
        # init_page返回值为mainpage对象，即首页
        mainpage = init_page
        with allure.step('1-添加商品'):
            product_name = f'自动化{ran_str(5)}'
            mainpage.to_prodcutAdd_page().add_product('1', '1', product_name, '成功', '1')
        with allure.step('2-跳转至商品列表页面'):
            time.sleep(3)
            product_list_page = mainpage.to_productList_page()
        with allure.step('3-获取商品列表第一个商品名称'):
            first_product_name = product_list_page.first_product_name_txt()
        with allure.step('4-断言'):
            assert first_product_name == product_name


if __name__ == '__main__':
    pytest.main(['test_addProduct.py', '-s', '--alluredir', reports_path, '--clean-alluredir'])
    os.system(f'allure serve {reports_path}')
