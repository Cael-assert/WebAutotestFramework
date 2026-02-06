from selenium.webdriver.common.by import By
from base.base_page import BasePage


class BingPage(BasePage):
    # 页面元素的位置的定义，放在元组中
    search_input_loc= (By.NAME, "q")
    # 定义一个具体的搜索业务
    def search_action(self,keyword):
        el = self.wait_and_find_element(self.search_input_loc)
        el.send_keys(keyword)
        el.submit()