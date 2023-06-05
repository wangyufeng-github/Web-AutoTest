# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/26 14:34
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : addProductKindPage.py
# @Software : PyCharm
import time

from common.basePage import BasePage


class AddProductKindPage(BasePage):
    """
    添加商品分类
    """

    def add_product_kind(self, kind_name, kind_idx, number, show, show_navigation, show_home_page, action=None):
        """
        添加商品分类
        :param kind_name:分类名称
        :param kind_idx:上级分类
        :param number:数量
        :param show:是否展示
        :param show_navigation:是否展示在导航栏
        :param show_home_page:是否展示在主页
        :param action:
        :return:
        """
        # 输入分类名称
        time.sleep(2)
        self.input_text(self.cate_name_input, kind_name)
        # 点击上级分类
        self.click(self.kind_select)
        # 选择上级分类
        self.kind_select_idx[-1] = self.kind_select_idx[-1].replace("%s", kind_idx)
        # 数量单位
        self.input_text(self.number_input, number)
        # 是否显示
        self.is_show[-1] = self.is_show[-1].replace("%s", show)
        self.click(self.is_show)
        # 是否展示导航栏
        self.is_show_navigation[-1] = self.is_show_navigation[-1].replace("%s", show_navigation)
        self.click(self.is_show_navigation)
        # 是否展示在首页
        self.is_show_home_page[-1] = self.is_show_home_page[-1].replace("%s", show_home_page)
        self.click(self.is_show_home_page)
        self.click(self.submit_btn)
        self.click(self.primary_submit_btn)
