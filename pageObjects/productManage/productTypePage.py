# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/29 9:20
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : productTypePage.py
# @Software : PyCharm
from common.basePage import BasePage


class ProductTypePage(BasePage):
    """
    商品类型界面
    """

    def add_product_type(self, type_name, list_style_idx, is_show_on_home,
                         img_path=None):
        """
        添加商品类型
        :param type_name:类型名称
        :param list_style_idx: 列表样式
        :param is_show_on_home: 是否展示在首页
        :param img_path: 图片路径
        :return:
        """
        # 添加按钮
        self.click(self.add_product_kind_btn)
        # 输入商品名称
        self.input_text(self.type_name_input, type_name)
        if img_path is not None:
            self.input_text(self.type_ico_upload_btn, img_path)
        # 选择列表样式
        self.list_style_radio_btn[-1] = self.list_style_radio_btn[-1].replace("%s", list_style_idx)
        # 点击对应的样式
        self.click(self.list_style_radio_btn)
        # 勾选是否展示在首页
        self.is_show_on_home_btn[-1] = self.is_show_on_home_btn[-1].replace("%s", is_show_on_home)
        self.click(self.is_show_on_home_btn)
        # 点击确定
        self.click(self.confirm_btn)

    def get_total_number(self):
        """
        获取商品类型总数
        :return:
        """
        total = self.get_text(self.total_number).split(" ")[1]
        return total
