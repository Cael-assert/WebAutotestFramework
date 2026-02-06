from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def wait_and_find_element(self,loc):
        wait = WebDriverWait(self.driver, 10)
        el = wait.until(EC.presence_of_element_located(loc))
        return el
