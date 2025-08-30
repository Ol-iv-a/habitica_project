import allure
from selene import browser, have
from pages.ui.application_manager import ApplicationManager


# def test_registration():
#     app = ApplicationManager()
#     app.home_page.register('Test123', 'firpo@powerscrews.com', '0a+qPV4a')
#     assert browser.element('#modal-body').should(have.text(' Добро пожаловать в '))

@allure.feature("Авторизация")
@allure.title("Авторизация с email (успешная)")
@allure.description("Проверяем успешную авторизацию, зная email и password пользователя")
@allure.tag("WEB", 'SUCCESS')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://habitica.com/", name="Website")
def test_login_with_email(browser_config):
    app = ApplicationManager()
    app.home_page.go_to_login()
    app.login_page.login_with_email('firpo@powerscrews.com', '0a+qPV4a')
    assert browser.element('.create-task-area').should(have.text('Добавить задачу'))

@allure.feature("Авторизация")
@allure.title("Авторизация с email (неуспешная)")
@allure.description("Проверяем валидацию при неуспешной авторизации по email")
@allure.tag("UI", 'FAILED')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://habitica.com/", name="Website")
def test_login_with_email_fail(browser_config):
    app = ApplicationManager()
    app.home_page.go_to_login()
    app.login_page.login_with_email('firpo1@powerscrews.com', '0a+qPV4a')

    browser.element('.error.positive').should(have.text('Ой-ой - ваш адрес электронной почты /'
                                                        ' логин или пароль неверный. - Убедитесь в том, '
                                                        'что они введены верно. Введите ваш логин и пароль '
                                                        'с учётом регистра. - Возможно, вы регистрировались '
                                                        'через Facebook или Google, а не по адресу электронной '
                                                        'почты. Перепроверьте еще раз. - Если вы забыли свой пароль, '
                                                        'кликните «Напомнить пароль».'))


@allure.feature("Авторизация")
@allure.title("Авторизация с username (успешная)")
@allure.description("Проверяем успешную авторизацию, зная username и password пользователя")
@allure.tag("UI", 'SUCCESS')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://habitica.com/", name="Website")
def test_login_with_username(browser_config):
    app = ApplicationManager()

    app.home_page.go_to_login()
    app.login_page.login_with_username('Test12', '0a+qPV4a')

    assert browser.element('.create-task-area').should(have.text('Добавить задачу'))


@allure.feature("Авторизация")
@allure.title("Авторизация с username (неуспешная)")
@allure.description("Проверяем валидацию при неуспешной авторизации по username")
@allure.tag("UI", 'FAILED')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://habitica.com/", name="Website")
def test_login_with_username_fail(browser_config):
    app = ApplicationManager()
    app.home_page.go_to_login()
    app.login_page.login_with_username('Test123', '0a+qPV4a')
    browser.element('.error.positive').should(have.text('Ой-ой - ваш адрес электронной почты /'
                                                        ' логин или пароль неверный. - Убедитесь в том, '
                                                        'что они введены верно. Введите ваш логин и пароль '
                                                        'с учётом регистра. - Возможно, вы регистрировались '
                                                        'через Facebook или Google, а не по адресу электронной '
                                                        'почты. Перепроверьте еще раз. - Если вы забыли свой пароль, '
                                                        'кликните «Напомнить пароль».'))
