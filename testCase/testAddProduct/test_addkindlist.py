# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/30 14:15
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : test_addkindlist.py
# @Software : PyCharm
import time, os, pytest, allure
from utils.handle_num import ran_str
from utils.handle_path import reports_path

"""
测试思路：
1-进入商品分类界面
2-添加商品分类
3-返回商品分类列表
4-切换最后一个分类，查看是否与新建分类一致
"""


@allure.epic('宝利商城-V2.0')
@allure.feature('商品管理')
class TestAddClassificationListCase:
    """
    添加商品分类
    """

    @allure.story('商品分类页面')
    def test_add_kind(self, init_page):
        mainpage = init_page
        with allure.step('1-进入商品分类界面添加商品分类'):
            class_name = '自动化%s' % ran_str(5)
            mainpage.to_productkind_page().to_add_prod_kind_page().add_product_kind(class_name, '2', 2, '1', '1', '1')
        with allure.step('2-进入商品分类界面获取最后一个分类名称'):
            last_name = mainpage.to_productkind_page().get_last_kind_name()
        with allure.step('3-判断最后一个分类名称是否正确'):
            assert last_name == class_name


if __name__ == '__main__':
    pytest.main(['test_addkindlist.py','-sv','--alluredir',reports_path,'--clean-alluredir'])
    os.system(f'allure serve {reports_path}')
