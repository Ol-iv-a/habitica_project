import os

import pytest
from selene import browser

from utils import allure_attach
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.base_url = "https://habitica.com"
    browser.config.window_height = 1440
    browser.config.window_width = 1400

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    selenoid_url = os.getenv("SELENOID_URL")
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")


    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options)

    browser.config.driver = driver

    yield browser

    allure_attach.get_screenshot(browser)
    allure_attach.get_logs(browser)
    allure_attach.get_html(browser)
    allure_attach.get_video(browser)
    browser.quit()