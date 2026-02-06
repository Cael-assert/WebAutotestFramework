import os

import pytest
from selenium import webdriver
import time

from common.yaml_util import read_yaml
from pages.bing_page import BingPage
# 数据路径设置
current_dir = os.path.dirname(os.path.abspath(__file__))
yaml_path = os.path.join(current_dir, '..','data','search_data.yaml')
# 读取刚才写好的两条数据
data_list = read_yaml(yaml_path)
# 把两条数据分别喂给测试用例跑两次
@pytest.mark.parametrize("case", data_list)
def test_bing_search(case):
    driver = webdriver.Chrome()
    driver.get("https://cn.bing.com")

    # 找到搜索框 (Bing的搜索框name通常是'q')
    bing = BingPage(driver)
    bing.search_action(case["search_term"])

    time.sleep(2)  # 简单等待看下效果
    assert case["expected"] in driver.title

    driver.quit()