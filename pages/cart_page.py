from selenium.webdriver.common.by import By

from base.base_page import BasePage


class CartPage(BasePage):
    item_name_locator = (By.CLASS_NAME, "inventory_item_name")

    def get_first_item_name(self):
        # 找到元素并提取它的文本内容(text)
        element = self.wait_and_find_element(self.item_name_locator)
        return element.text