import os
import allure
from pages.api.auth_page import AuthPage


@allure.feature("Авторизация")
@allure.title("Успешная авторизация")
@allure.description("Проверяем успешную авторизацию под существующим пользователем")
@allure.tag("API", 'SUCCESS')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(os.getenv('BASE_URL') + os.getenv('LOGIN_ENDPOINT'))
def test_login():
    auth_page = AuthPage()
    r = auth_page.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))
    with allure.step('Проверить, что статус код = 200'):
        assert r.status_code == 200
    with allure.step('Проверить, что пришел apiToken'):
        assert r.json()['data']['apiToken']


@allure.feature("Авторизация")
@allure.title("Неуспешная авторизация")
@allure.description("Проверяем текст ошибки при авторизацию под несуществующим пользователем")
@allure.tag("API", 'FAILED')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(os.getenv('BASE_URL') + os.getenv('LOGIN_ENDPOINT'))
def test_login_fail():
    auth_page = AuthPage()
    r = auth_page.login("fail@powerscrews.com", "0a+qPV4a")
    with allure.step('Проверить, что статус код = 401'):
        assert r.status_code == 401
    with allure.step('Проверить текст ошибки'):
        assert r.json()['message'] == ('Uh-oh - your email address / username or password is incorrect.\n'
                                          '- Make sure they are typed correctly. Your username and password '
                                          'are case-sensitive.\n- You may have signed up with Facebook or Google-sign-in, '
                                          'not email so double-check by trying them.\n- If you forgot your password, click '
                                          '\"Forgot Password\".')
