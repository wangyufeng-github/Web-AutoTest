# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/29 14:16
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : conftest.py
# @Software : PyCharm
import pytest
import time

from configs.config import username, password
from pageObjects.loginPage import LoginPage


@pytest.fixture(scope='session')
def init_page():
    print('宝利商场--商品管理模块自动化执行------')
    # 首页
    mainpage = LoginPage().to_login_page().login(username, password)
    yield mainpage
    """
    mainpage:MainPage()   首页
    mainpage.to_productlist_page():ProductListPage()  商品列表页面
    
    conftest文件路径不同时，先执行外层conftest，再执行模块内部conftest，若存在同名方法，优先执行模块内部的
    yield关键字上面的则在用例执行前执行，下面的在在用例执行完再执行
    """
    # 删除第一个商品
    # mainpage.to_productList_page().delete_first_product()
    time.sleep(3)
    mainpage.to_home_page()
    print('宝利商场--商品管理模块自动化执行结束------')
