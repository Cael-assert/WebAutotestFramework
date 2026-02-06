from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage):
    # 定义定位符（元组配置）
    user_input = (By.ID,"user-name")
    pwd_input = (By.ID,"password")
    login_btn = (By.ID,"login-button")
    def login_action(self,username,password):
        el1 = self.wait_and_find_element(self.user_input)
        el1.send_keys(username)
        el2 = self.wait_and_find_element(self.pwd_input)
        el2.send_keys(password)
        el3 = self.wait_and_find_element(self.login_btn)
        el3.click()