# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/31 14:27
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : test_addproductattr.py
# @Software : PyCharm
import pytest, time, os, allure
from utils.handle_num import ran_str
from utils.handle_path import reports_path

"""
1-切换到商品规格界面
2-添加商品属性
3-判断商品规格页面第一个属性名称是否与设置一致
"""


@allure.epic('宝利商城-V2.0')
@allure.feature('商品管理')
class TestAddProductAttribute:
    @allure.feature('添加商品属性')
    def test_addproduct_attribute(self, init_page):
        mainpage = init_page
        with allure.step('1-进入商品规格页面,添加商品属性'):
            attribute_name = '自动化测试：%s' % ran_str(5)
            attribute_page = mainpage.to_productattr_page().to_add_productattribute_page()
            time.sleep(3)
            attribute_page.add_product_attr(attribute_name, '1', '1')
        with allure.step('2-获取商品规格页面所有商品属性'):
            time.sleep(3)
            all_att_name = mainpage.to_productattr_page().get_all_ttribute_name()
        with allure.step('3-断言'):
            assert attribute_name in all_att_name


if __name__ == '__main__':
    pytest.main(['test_addproductattr.py', '-s', '--alluredir', reports_path, '--clean-alluredir'])
    os.system(f'allure serve {reports_path}')
