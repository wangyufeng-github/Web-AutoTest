# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/26 14:57
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : productAttributePage.py
# @Software : PyCharm
from common.basePage import BasePage
from pageObjects.productManage.addproductAttributePage import AddProductAttributePage


class ProductAttributePage(BasePage):
    """
    商品规格界面
    """

    def get_all_ttribute_name(self):
        """
        获取所有商品属性名称
        :return:
        """
        all_attr_name = self.get_text(self.all_attr_name_txt, many=True)
        return all_attr_name

    def to_add_productattribute_page(self):
        """
        点击添加按钮，进入商品属性增加界面
        :return:
        """
        self.click(self.add_btn)
        return AddProductAttributePage()
