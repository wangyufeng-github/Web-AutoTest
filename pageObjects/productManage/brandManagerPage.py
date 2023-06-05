# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/26 14:49
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : brandManagerPage.py
# @Software : PyCharm
from common.basePage import BasePage


class BrandManagerPage(BasePage):
    """
    品牌管理界面
    """

    def search_brand(self, brand_name):
        """
        查询品牌
        :param brand_name:
        :return:
        """
        self.input_text(self.brand_search_input, brand_name)
        self.click(self.search_btn)

    def get_first_brand(self):
        first_brand = self.get_text(self.first_brand_name_txt)
        return first_brand

    def get_all_brand(self):
        all_brands = self.get_text(self.all_brand_name_txt, many=True)
        return all_brands
