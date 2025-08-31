import os

import pytest
from selene import browser

from utils import allure_attach
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def is_remote_run():
    return os.getenv("RUN_MODE", "local").lower() == "remote"


@pytest.fixture
def browser_config():
    if is_remote_run():
        browser = create_remote_browser()
    else:
        browser = create_local_browser()

    yield browser

    if is_remote_run():
        # allure_attach.get_video(browser)
        # allure_attach.get_remote_log(browser)
    else:
        allure_attach.get_screenshot(browser)
        allure_attach.get_logs(browser)
        allure_attach.get_html(browser)
    browser.quit()


def create_local_browser():
    browser.config.base_url = "https://habitica.com"
    browser.config.window_height = 1440
    browser.config.window_width = 1400
    # options = webdriver.ChromeOptions()
    # options.add_argument("--start-maximized")
    # return webdriver.Chrome(options=options)
    return browser

def create_remote_browser():
    browser.config.base_url = "https://habitica.com"
    browser.config.window_height = 1440
    browser.config.window_width = 1400
    options = Options()
    options.add_argument("--lang=ru")
    options.add_argument("--accept-lang=ru")
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    selenoid_url = os.getenv("SELENOID_URL")
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options)

    browser.config.driver = driver

    yield browser

# @pytest.fixture(scope='function', autouse=True)
# def browser_config():
#     browser.config.base_url = "https://habitica.com"
#     browser.config.window_height = 1440
#     browser.config.window_width = 1400
#
#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": "128.0",
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": True,
#             "enableLog": True
#         }
#     }
#     selenoid_url = os.getenv("SELENOID_URL")
#     selenoid_login = os.getenv("SELENOID_LOGIN")
#     selenoid_pass = os.getenv("SELENOID_PASS")
#
#
#     options.capabilities.update(selenoid_capabilities)
#     driver = webdriver.Remote(
#         command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
#         options=options)
#
#
#     browser.config.driver = driver
#
#     yield browser
#
#     allure_attach.get_screenshot(browser)
#     allure_attach.get_logs(browser)
#     allure_attach.get_html(browser)
#     allure_attach.get_video(browser)
#     browser.quit()