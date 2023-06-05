# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/19 11:38
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : addProductPage.py
# @Software : PyCharm
from common.basePage import BasePage


class AddProductPage(BasePage):
    """
    添加商品页面
    """

    def add_product(self, idx1, idx2, product_name, subtitle, brand_select_idx):
        """
        添加商品
        :param idx1:一级分类
        :param idx2:二级分类
        :param product_name:商品名称
        :param subtitle:副标题
        :param brand_select_idx:商品品牌
        :return:
        """
        # 商品分类下拉框
        self.click(self.product_kind_select)
        # 将元素定位中的品牌名称通过参数的形式改变
        self.product_kind_select_index1[-1] = self.product_kind_select_index1[-1].replace('%s', idx1)
        # 点击商品分类一级标题
        self.click(self.product_kind_select_index1)
        # 改变二级分类
        self.product_kind_select_index2[-1] = self.product_kind_select_index2[-1].replace('%s', idx2)
        # 点击二级分类
        self.click(self.product_kind_select_index2)
        # 输入商品名称
        self.input_text(self.product_name, product_name)
        # 输入副标题
        self.input_text(self.product_subtitle, subtitle)
        # 点击商品品牌
        self.click(self.product_brand_select)
        # 选择商品品牌
        self.product_brand_select_idx[-1] = self.product_brand_select_idx[-1].replace('%s', brand_select_idx)
        self.click(self.product_brand_select_idx)
        # 点击下一步，填写商品促销
        self.click(self.next_commodity_promotion_btn)
        # 点击是否预告商品开关
        self.click(self.is_herald)
        # 点击[下一步, 填写商品属性]按钮
        self.click(self.next_product_attribute_btn)
        # 点击下一步, 选择商品关联按钮
        self.click(self.netxt_product_related_btn)
        # 点击完成,提交商品按钮
        self.click(self.complete_btn)
        # 确认提交
        self.click(self.submit_btn)
