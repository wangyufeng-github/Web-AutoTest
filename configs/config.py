# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/17 14:27
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : config.py
# @Software : PyCharm
import os
url = 'http://124.223.33.41:38090/#/login'
# 设置隐式等待时间10s，即页面所有元素加载时间为10s
implicitly_wait = 10
username = '朝天宫134'
password = '123456'
chrome_driver_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\\drivers\\chromedriver.exe'

