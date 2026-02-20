import os
import time

import pytest
from selenium import webdriver

from common.logger import get_logger

logger = get_logger("Conftest")
# 第一次新增：Fixture驱动管理
@pytest.fixture()
def get_driver(request):
    options = webdriver.ChromeOptions()
    # 关闭密码保存提示，关闭密码泄露警告
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    # yield之前是“前置操作”
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    # 第一次新增：核心纽带把driver绑定在当前的测试用例节点上
    # 第一次新增：后面的Hook钩子就能在用例失败时，从节点上拿到driver去截图
    request.node.driver = driver
    yield driver
    driver.quit()

# --第一次新增：Pytest魔法钩子：失败自动截图--
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 获取当前用例的执行结果
    outcome = yield
    report = outcome.get_result()
    # 核心判断逻辑：如果这个用例是在执行阶段(call)且结果是失败的(failed)
    if report.when == "call" and report.failed:
        logger.error(f"检测到用例失败：{item.name},准备截图...")
        # 第一次新增：从刚才绑定的节点上把driver拿出来
        driver = getattr(item, "driver", None)
        if driver:
            # 动态生成截图保存路径(放在根目录的screenshots文件夹下)
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            screenshot_dir = os.path.join(base_dir, "screenshots")
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            # 第一次新增：使用时间戳命名图片，防止被覆盖
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            pic_name = f"{item.name}-{timestamp}.png"
            pic_path = os.path.join(screenshot_dir, pic_name)
            # 执行截图
            driver.get_screenshot_as_file(pic_path)
            logger.info(f"现场截图已保存至：{pic_path}")