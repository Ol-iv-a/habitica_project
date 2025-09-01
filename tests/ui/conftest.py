import os

import pytest
from selene import browser

from utils import allure_attach
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def is_remote_run():
    return os.getenv("RUN_MODE", "local").lower() == "remote"

def create_local_driver():
    """Создание локального драйвера Chrome"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)

def create_remote_driver():
    """Создание удаленного драйвера для Selenoid"""
    options = Options()
    options.add_argument("--lang=ru")
    options.add_argument("--accept-lang=ru-RU,ru")

    # Настройка capabilities для Selenoid
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

    # Получение учетных данных из переменных окружения
    selenoid_url = os.getenv("SELENOID_URL")
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")

    # Создание удаленного драйвера
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options
    )

    return driver


@pytest.fixture(scope="function")
def browser_config():
    """Фикстура для настройки браузера (локального или удаленного)"""
    # Создаем драйвер в зависимости от режима запуска
    if is_remote_run():
        driver = create_remote_driver()
    else:
        driver = create_local_driver()

    # Настройка Selene
    browser.config.driver = driver
    browser.config.base_url = "https://habitica.com"
    browser.config.window_width = 1400
    browser.config.window_height = 1440
    browser.config.timeout = 10

    yield browser
    # Прикрепление артефактов после выполнения теста
    if is_remote_run():
        # Для удаленного запуска - видео и логи Selenoid
        allure_attach.get_video(browser)
        allure_attach.get_remote_log(browser)
    else:
        # Для локального запуска - скриншот, логи браузера и HTML
        allure_attach.get_screenshot(browser)
        allure_attach.get_logs(browser)
        allure_attach.get_html(browser)

    # Закрытие браузера
    browser.quit()

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