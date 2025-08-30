import os

import allure
import requests
from dotenv import load_dotenv

load_dotenv()

class AuthPage:
    def __init__(self):
        self.base_url = os.getenv('BASE_URL')
        self.login_url = self.base_url + os.getenv('LOGIN_ENDPOINT')

    @allure.step('Выполнить запрос на авторизацию')
    def login(self, username, password):
        response = requests.post(self.login_url, json={"username": username, "password": password})

        with allure.step("Лог: url и тело запроса"):
            allure.attach(body=response.request.url, name='Request URL')
            allure.attach(name="Request Body", body=response.request.body,
                          attachment_type=allure.attachment_type.JSON)
        with allure.step("Лог: статус код и тело ответа"):
            allure.attach(body=str(response.status_code), name='Status Code',
                          attachment_type=allure.attachment_type.JSON)
            allure.attach(body=response.text, name='Response Body', attachment_type=allure.attachment_type.JSON)
        return response


    def login_and_get_headers(self, username, password):
        user = {
            "username": username,
            "password": password
        }

        headers = {
            "x-client": "habitica-web"
        }

        response = requests.post(self.login_url, json=user, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Ошибка аутентификации: {response.status_code} - {response.text}")

        api_user = response.json()['data'].get('id')
        api_key = response.json()['data'].get('apiToken')
        auth_headers = {
            "x-api-user": api_user,
            "x-api-key": api_key,
            "x-client": "habitica-web"
        }
        return auth_headers