from selenium.webdriver.common.by import By

from base.base_page import BasePage



class ProductsPage(BasePage):
    add_cart_btn = (By.CSS_SELECTOR,"[id^='add-to-cart']")
    # 验证是否加购成功
    cart_link = (By.CSS_SELECTOR,".shopping_cart_link")

    def add_first_item(self):
        cl1 = self.wait_and_find_element(self.add_cart_btn)
        cl1.click()
        cl2 = self.wait_and_find_element(self.cart_link)
        cl2.click()