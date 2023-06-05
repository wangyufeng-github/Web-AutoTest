# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/26 15:35
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : productListPage.py
# @Software : PyCharm
import time

from common.basePage import BasePage


class ProductListPage(BasePage):
    """
    商品列表界面
    """

    def first_product_name_txt(self):
        """
        第一行商品名称
        :return:
        """
        first_product_name = self.get_text(self.first_product)
        return first_product_name

    def product_name_txt(self):
        """
        获取所有商品名称
        :return:
        """
        all_products = self.get_text(self.all_products, many=True)
        return all_products

    def product_brands_txt(self):
        """
        获取所有商品品牌
        :return:
        """
        all_product_brands = self.get_text(self.all_product_brands, many=True)
        return all_product_brands

    def reset(self):
        """
        点击重置按钮
        :return:
        """
        self.click(self.search_rest)
        return self

    def search_product(self, product_name=None, product_brand_search=False,
                       shelves_status_search=False):
        # 判断商品名称是否真
        if product_name:
            self.input_text(self.product_name_search_input, product_name)
        if product_brand_search:
            self.click(self.product_brand_search_select)
            time.sleep(2)
            self.text = "品牌：" + self.get_text(self.product_brand_search_select_idx1)
            # 选择第一个商品品牌
            self.click(self.product_brand_search_select_idx1)
            # 判断商品上架状态
        if shelves_status_search:
            # 点击上架状态
            self.click(self.shelves_status_select)
            # 选择第一个【上架】
            self.click(self.shelves_status_select_idx)
        # 点击搜索按钮
        self.click(self.search_button)
        return self

    def delete_first_product(self):
        """
        删除第一个商品
        :return:
        """
        # 勾选第一个商品
        self.click(self.select_first)
        # 点击删除
        self.click(self.delete_btn)
        # 点击确定
        self.click(self.delete_ascertain)
        return self


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://124.223.33.41:38090/#/pms/product")
    time.sleep(3)
    driver.find_element_by_id("username").send_keys("朝天宫134")
    driver.find_element_by_id("password").send_keys('123456')
    driver.find_element_by_id("btnLogin").click()
    time.sleep(2)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_css_selector("#app > div > div.main-container > ul > div.hamburger-container > svg").click()
    time.sleep(2)
    # driver.find_element_by_css_selector("li:nth-child(2) > div").click()

    # 商品管理
    driver.find_element_by_css_selector('li:nth-child(2) > div').click()
    time.sleep(2)
    # 商品列表
    driver.find_element_by_css_selector('a[href="#/pms/product"]').click()

    time.sleep(2)
    # 商品品牌
    driver.find_element_by_css_selector('form >div:nth-child(3) .el-input__inner').click()
    time.sleep(2)
    print(driver.find_element_by_css_selector('body > .el-select-dropdown ul > li:nth-child(1)').text)
