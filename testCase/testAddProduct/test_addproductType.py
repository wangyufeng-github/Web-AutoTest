# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/31 15:10
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : test_addproductType.py
# @Software : PyCharm
import pytest, allure, os, time
from utils.handle_num import ran_str
from utils.handle_path import reports_path

"""
1-切换商品类型页面获取总数
2-添加商品类型
3-再次获取类型总数
4-断言数量是否增加
"""


@allure.epic('宝利商城-V2.0')
@allure.feature('商品管理')
class TestProductTypeCase:
    @allure.story('添加商品类型')
    def test_add_product_type(self, init_page):
        mainpage = init_page
        with allure.step('1-获取商品类型总数'):
            product_type_obj = mainpage.to_product_type_page()
            time.sleep(3)
            total_before = product_type_obj.get_total_number()
        with allure.step('2-添加商品类型'):
            product_type_obj.add_product_type(str(time.time()), '1', '1')
        with allure.step('3-重新获取商品类型总数'):
            time.sleep(2)
            total_after = product_type_obj.get_total_number()
        with allure.step('4-断言'):
            assert int(total_before) == int(total_after) - 1


if __name__ == '__main__':
    pytest.main(['test_addproductType.py', '-sv', '--alluredir', reports_path, '--clean-alluredir'])
    os.system(f'allure serve {reports_path}')
