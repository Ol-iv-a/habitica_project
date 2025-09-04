import allure
from selene import browser
from time import sleep


class LoginPage:
    def __init__(self):
        self.username = browser.element('#usernameInput')
        self.password = browser.element('#passwordInput')
        self.sing_in_button = browser.element('.btn.btn-info')

    @allure.step('Авторизоваться с email')
    def login_with_email(self, email, password):
        sleep(1)
        self.username.set_value(email)
        self.password.set_value(password)
        sleep(2)
        self.sing_in_button.click()
        return self

    @allure.step('Авторизоваться с username')
    def login_with_username(self, username, password):
        sleep(1)
        self.username.set_value(username)
        self.password.set_value(password)
        sleep(2)
        self.sing_in_button.click()
        return self