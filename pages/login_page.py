from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.base_page import BasePage


class LoginPage(BasePage):
    # 定义定位符（元组配置）
    user_input = (By.ID, "user-name")
    pwd_input = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    error_msg_loc = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login_action(self, username, password):
        el1 = self.wait_and_find_element(self.user_input)
        el1.clear()
        el1.send_keys(username)
        el2 = self.wait_and_find_element(self.pwd_input)
        el2.clear()
        el2.send_keys(password)
        el3 = self.wait_and_find_element(self.login_btn)
        el3.click()

    def login_action_press_enter(self, username, password):
        """输入账号密码后按回车键登录"""
        el1 = self.wait_and_find_element(self.user_input)
        el1.clear()
        el1.send_keys(username)
        el2 = self.wait_and_find_element(self.pwd_input)
        el2.clear()
        el2.send_keys(password)
        el2.send_keys(Keys.ENTER)

    def get_error_message(self):
        el = self.wait_and_find_element(self.error_msg_loc)
        return el.text

    def is_login_success(self):
        """通过 URL 是否包含 inventory 判断是否登录成功"""
        return "inventory" in self.driver.current_url

    def get_username_value(self):
        el = self.wait_and_find_element(self.user_input)
        return el.get_attribute("value") or ""

    def get_password_value(self):
        el = self.wait_and_find_element(self.pwd_input)
        return el.get_attribute("value") or ""
