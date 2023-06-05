# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/31 16:09
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : test_searchProduct.py
# @Software : PyCharm

import os
import time
import allure
import pytest
from utils.handle_path import reports_path

"""
1-商品列表
2-输入搜索-自动化
3-商品品牌：春装
"""


@allure.epic('宝利商城-V2.0')  # 工程级别
@allure.feature('商品管理')
class TestSearchProduct:
    @allure.story('搜索商品名称')
    def test_search_product_name(self, init_page):
        """根据名称搜索商品"""
        with allure.step("输入商品名称"):
            # 进入商品列表页面
            mainpage = init_page
            time.sleep(3)
            productlist = mainpage.to_productList_page()
            product_name = "test"
            # 描述一段文本进测试报告
            allure.attach("新增的商品名称是%s" % product_name, "./a.txt", attachment_type=allure.attachment_type.TEXT)
        with allure.step('根据商品名称搜索'):
            # 根据商品名称搜索
            time.sleep(3)
            productlist_obj = productlist.search_product(product_name=product_name)
            time.sleep(5)
            products = productlist_obj.product_name_txt()
            productlist_obj.reset()
        with allure.step('执行断言'):
            assert product_name in products

    @allure.story('根据商品品牌')
    def test_search_product_by_brand(self, init_page):
        with allure.step("选择品牌"):
            # 进入商品列表页面
            mainpage = init_page
            time.sleep(3)
            productlist = mainpage.to_productList_page()
            prdocutlist_obj = productlist.search_product(product_brand_search=True)
            # time.sleep(3)
            # prdocutlist_obj._driver.get_screenshot_as_file("./a.png")
            # allure.attach.file("./a.png", attachment_type=allure.attachment_type.PNG)
        with allure.step("执行断言"):
            time.sleep(3)
            product_brands = prdocutlist_obj.product_brands_txt()
            assert prdocutlist_obj.text in product_brands


if __name__ == '__main__':
    pytest.main(['test_searchProduct.py', '-s', '--alluredir', reports_path, '--clean-alluredir'])
    os.system(f'allure serve {reports_path}')
