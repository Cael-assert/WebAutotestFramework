from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.logger import log
class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def wait_and_find_element(self,loc,timeout=10):
        log.info(f"正在查找元素:{loc}")
        try:
            wait = WebDriverWait(self.driver, timeout)
            el = wait.until(EC.presence_of_element_located(loc))
            return el
        except Exception as e:
            log.error(f"查找元素超时失败:{loc}")
            raise e
