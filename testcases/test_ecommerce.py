import os
import time

import pytest
from selenium import webdriver

from common.yaml_util import read_yaml
from config.settings import BASE_URL
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
# 精确读取YAML数据
current_dir = os.path.dirname(os.path.abspath(__file__))
yaml_path = os.path.join(current_dir, '..','data','search_data.yaml')
data_list = read_yaml(yaml_path)

@pytest.mark.parametrize("case", data_list)
def test_saucedemo_workflow(case,get_driver):
    driver = get_driver
    driver.get(BASE_URL)
    # 核心链路阶段1：登录
    login_page = LoginPage(driver)
    login_page.login_action(case["user"], case["pwd"])
    # 核心链路阶段2：架构与断言

    if case["user"] == "standard_user":
        products_page = ProductsPage(driver)
        products_page.add_first_item()
        # 实例化购物车页面，获取里面的商品名称
        cart_page = CartPage(driver)
        actual_item_name = cart_page.get_first_item_name()
        assert "Sauce Labs Backpack" in actual_item_name
        checkout_page = CheckoutPage(driver)
        res_text = checkout_page.finish_checkout("Liu", "Yunkai", "450000")
        time.sleep(2)
        assert "Thank you for your order" in res_text
    else:
        # 对于被锁定的用户，我们断言他依然停留在登录页url不变
        assert "saucedemo.com" in driver.current_url
