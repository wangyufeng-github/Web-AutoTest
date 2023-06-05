# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/25 10:37
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : addproductAttributePage.py
# @Software : PyCharm
from common.basePage import BasePage


class AddProductAttributePage(BasePage):
    """
    商品规格->添加商品属性
    """

    def add_product_attr(self, attr_name, idx, idx1):
        """
        增加商品属性
        """
        # 分类名称
        self.input_text(self.attr_name_input, attr_name)
        # 上级分类
        self.click(self.type_select)
        self.type_select_idx[-1] = self.type_select_idx[-1].replace("%s", idx)
        # 选择商品分类
        self.click(self.type_select_idx)
        # 筛选属性
        self.product_type_radio[-1] = self.product_type_radio[-1].replace("%s", idx1)
        self.click(self.product_type_radio)
        # 提交
        self.click(self.submit_btn)
        # 确定
        self.click(self.sure_btn)
