import pytest
from selene import browser

from utils import allure_attach


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.base_url = "https://habitica.com"
    browser.config.window_height = 1440
    browser.config.window_width = 1400


    yield browser

    allure_attach.get_screenshot(browser)
    allure_attach.get_logs(browser)
    allure_attach.get_html(browser)
    allure_attach.get_video(browser)
    browser.quit()