# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/26 15:28
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : productKindPage.py
# @Software : PyCharm
import time

from common.basePage import BasePage
from pageObjects.productManage.addProductKindPage import AddProductKindPage


class ProductKindListPage(BasePage):
    """
    商品分类界面
    """

    def get_last_kind_name(self):
        self.click(self.last_page_btn)
        time.sleep(3)
        # 最后一行分类名称
        last_kind_name = self.get_text(self.last_kind_name)
        return last_kind_name

    def to_add_prod_kind_page(self):
        """
        通过点击添加，进入添加商品分类界面
        :return:
        """
        self.click(self.add_btn)
        return AddProductKindPage()
