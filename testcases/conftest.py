import pytest
from selenium import webdriver

@pytest.fixture()
def get_driver():
    # yield之前是“前置操作”
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()