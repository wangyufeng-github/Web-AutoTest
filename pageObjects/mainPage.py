# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/23 13:50
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : mainPage.py
# @Software : PyCharm
import time

from common.basePage import BasePage
from pageObjects.productManage.addProductPage import AddProductPage
from pageObjects.productManage.brandManagerPage import BrandManagerPage
from pageObjects.productManage.productAttributePage import ProductAttributePage
from pageObjects.productManage.productKindPage import ProductKindListPage
from pageObjects.productManage.productListPage import ProductListPage
from pageObjects.productManage.productTypePage import ProductTypePage


class MainPage(BasePage):
    """
    主要实现左侧菜单栏点击操作
    """

    def to_productList_page(self, action=None):
        """
        左侧菜单栏点击【商品管理】-【商品列表】
        :param action:
        :return:
        """
        # 点击商品管理
        self.click(self.product_admin_btn)
        # 点击商品列表
        self.click(self.product_list_btn)
        return ProductListPage()

    def to_prodcutAdd_page(self, action=None):
        """
        点击左侧添加商品
        :param action:
        :return:
        """
        # 商品管理
        self.click(self.product_admin_btn)
        # 添加商品
        self.click(self.product_add_btn)
        return AddProductPage()

    def to_login_page(self, action=None):
        """
        主页面退出操作
        :param action:
        :return:
        """
        # 右上角菜单栏
        self.click(self.login_out_btn)
        time.sleep(2)
        # 点击退出
        self.click(self.login_out_select)

    def to_home_page(self):
        """
        返回首页
        :return:
        """
        self.click(self.home_btn)

    def get_today_orders(self, action=None):
        """
        获取今日下单数
        :param action:
        :return:
        """
        return self.get_text(self.today_orders, action)

    def get_today_sales(self, action=None):
        """
        获取今日销售总额
        :param action:
        :return:
        """
        return self.get_text(self.today_sales, action)

    def get_today_product(self, action=None):
        """
        获取今日商品数
        :param action:
        :return:
        """
        return self.get_text(self.today_product, action)

    def get_today_members(self, action=None):
        """
        获取今日会员
        :param action:
        :return:
        """
        return self.get_text(self.today_members, action)

    def to_productkind_page(self, action=None):
        """
        前往商品分类界面
        :param action:
        :return:
        """
        self.click(self.product_admin_btn, action)
        self.click(self.product_kind_btn, action)
        return ProductKindListPage()

    def to_product_type_page(self, action=None):
        """
        前往商品类型界面
        :param action:
        :return:
        """
        self.click(self.product_admin_btn, action)
        self.click(self.product_type_btn, action)
        return ProductTypePage()

    def to_productattr_page(self, action=None):
        """
        商品规格界面
        :param action:
        :return:
        """
        self.click(self.product_admin_btn, action)
        self.click(self.product_attr_btn, action)
        return ProductAttributePage()

    def to_brand_manager_page(self, action=None):
        """
        品牌管理界面
        :param action:
        :return:
        """
        self.click(self.product_admin_btn, action)
        self.click(self.brand_manager_btn, action)
        return BrandManagerPage()


if __name__ == '__main__':
    pass
