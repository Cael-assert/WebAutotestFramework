import os

import pytest

from common.yaml_util import read_yaml
from config.settings import BASE_URL
from pages.login_page import LoginPage


# 正确加载 yaml：文件是「字典」结构，包含 login_abnormal / login_special_users / login_edge_cases 三个 key
current_dir = os.path.dirname(os.path.abspath(__file__))
yaml_path = os.path.join(current_dir, '..', 'data', 'login_data.yaml')
_all_data = read_yaml(yaml_path)

# 取出三组用例列表，共 19 条
abnormal_cases = _all_data["login_abnormal"]           # 11 条
special_user_cases = _all_data["login_special_users"]  # 4 条
edge_cases = _all_data["login_edge_cases"]             # 4 条


# ---------- 1. 异常登录校验（11 条）----------
@pytest.mark.parametrize("case", abnormal_cases)
def test_login_abnormal(case, get_driver):
    driver = get_driver
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login_action(case["username"], case["password"])

    actual_error = login_page.get_error_message()
    assert case["expected_error"] in actual_error


# ---------- 2. 特殊用户登录（4 条）：能登录成功即可 ----------
@pytest.mark.parametrize("case", special_user_cases)
def test_login_special_users(case, get_driver):
    driver = get_driver
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login_action(case["username"], case["password"])

    assert login_page.is_login_success(), (
        f"特殊用户 {case.get('case_id')} 应登录成功，expected_result={case.get('expected_result')}"
    )


# ---------- 3. 边界/操作类用例（4 条）----------
@pytest.mark.parametrize("case", edge_cases)
def test_login_edge_cases(case, get_driver):
    driver = get_driver
    driver.get(BASE_URL)
    login_page = LoginPage(driver)

    action = case.get("action", "click_login")

    if action == "refresh_page":
        # TC014：输入后刷新，校验输入框被清空
        login_page.refresh_clear_username_pwd(case["username"], case["password"])
        driver.refresh()
        login_page = LoginPage(driver)
        assert login_page.get_username_value() == case.get("expected_username_box", "")
        assert login_page.get_password_value() == case.get("expected_password_box", "")

    elif action == "press_enter_key":
        # TC015：输入后按回车登录
        login_page.login_action_press_enter(case["username"], case["password"])
        assert login_page.is_login_success()

    elif action == "browser_back_and_forward":
        # TC016：登录成功后后退再前进，仍保持登录
        login_page.login_action(case["username"], case["password"])
        assert login_page.is_login_success()
        driver.back()
        driver.forward()
        assert "inventory" in driver.current_url

    else:
        # TC017：点击登录（错误密码），校验失败后用户名保留、密码清空
        login_page.login_action(case["username"], case["password"])
        assert login_page.get_username_value() == case.get("expected_username_box", "")
        assert login_page.get_password_value() == case.get("expected_password_box", "")
