import allure
from selene import browser
from selene.support.shared.jquery_style import s

class HomePage:
    def __init__(self):
        self.username = s('#usernameInput')
        self.email = s('[placeholder="Электронная почта"]')
        self.password = s('[placeholder="Пароль"]')
        self.approve_password = s('[placeholder="Подтвердите пароль"]')
        self.move_to_login_button = s('[href="/login"]')
        self.sign_up_button = s('.btn.btn-block.btn-info.sign-up')

    @allure.step('Открыть главную страницу habitica.com')
    def open(self):
        browser.open('/')
        return self

    @allure.step('Переход на страницу авторизации')
    def go_to_login(self):
        self.open().move_to_login_button.click()
        return self

    def register(self, username, email, password):
        self.username.set_value(username).press_enter()
        self.email.set_value(email).press_enter()
        self.password.set_value(password).press_enter()
        self.approve_password.set_value(password)
        self.sign_up_button.click()