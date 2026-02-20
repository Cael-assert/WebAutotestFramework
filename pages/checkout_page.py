from selenium.webdriver.common.by import By

from base.base_page import BasePage


class CheckoutPage(BasePage):
    checkout_btn = (By.ID, "checkout")
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    zip_code = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    finish_btn = (By.ID, "finish")
    success_msg = (By.CLASS_NAME, "complete-header")

    def finish_checkout(self,f_name,l_name,post_code):
        self.wait_and_find_element(self.checkout_btn).click()
        self.wait_and_find_element(self.first_name).send_keys(f_name)
        self.wait_and_find_element(self.last_name).send_keys(l_name)
        self.wait_and_find_element(self.zip_code).send_keys(post_code)
        self.wait_and_find_element(self.continue_btn).click()
        self.wait_and_find_element(self.finish_btn).click()

        return self.wait_and_find_element(self.success_msg).text