import os

import allure
import requests


class TasksPage:
    def __init__(self, auth_headers):
        self.base_url = os.getenv('BASE_URL')
        self.tasks_user_url = self.base_url + os.getenv('TASKS_USER_ENDPOINT')
        self.tasks_url = self.base_url + os.getenv('TASKS_ENDPOINT')
        self.headers = auth_headers

    @allure.step('Выполнить запрос на получение задач пользователя')
    def get_user_tasks(self):
        response = requests.get(self.tasks_user_url, headers=self.headers)

        with allure.step("Лог: url"):
            allure.attach(body=response.request.url, name='Request URL')
        with allure.step("Лог: статус код и тело ответа"):
            allure.attach(body=str(response.status_code), name='Status Code',
                          attachment_type=allure.attachment_type.JSON)
            allure.attach(body=response.text, name='Response Body', attachment_type=allure.attachment_type.JSON)
        return response


    @allure.step('Выполнить запрос на получение задач пользователя по фильтру')
    def get_user_tasks_with_type_filter(self, type_filter):
        params = {'type': type_filter}
        response = requests.get(self.tasks_user_url, params=params, headers=self.headers)

        with allure.step("Лог: url"):
            allure.attach(body=response.request.url, name='Request URL')
        with allure.step("Лог: статус код и тело ответа"):
            allure.attach(body=str(response.status_code), name='Status Code',
                          attachment_type=allure.attachment_type.JSON)
            allure.attach(body=response.text, name='Response Body', attachment_type=allure.attachment_type.JSON)
        return response


    @allure.step('Выполнить запрос на получение задач пользователя по task_id')
    def get_user_task_by_id(self, task_id):
        response = requests.get(f"{self.tasks_url}/{task_id}", headers=self.headers)

        with allure.step("Лог: url"):
            allure.attach(body=response.request.url, name='Request URL')
        with allure.step("Лог: статус код и тело ответа"):
            allure.attach(body=str(response.status_code), name='Status Code',
                          attachment_type=allure.attachment_type.JSON)
            allure.attach(body=response.text, name='Response Body', attachment_type=allure.attachment_type.JSON)
        return response


    @allure.step('Выполнить запрос на создание задачи')
    def create_task(self, task_data):
        response = requests.post(self.tasks_user_url, json=task_data, headers=self.headers)

        with allure.step("Лог: url и тело запроса"):
            allure.attach(body=response.request.url, name='Request URL')
            allure.attach(name="Request Body", body=response.request.body,
                          attachment_type=allure.attachment_type.JSON)
        with allure.step("Лог: статус код и тело ответа"):
            allure.attach(body=str(response.status_code), name='Status Code',
                          attachment_type=allure.attachment_type.JSON)
            allure.attach(body=response.text, name='Response Body', attachment_type=allure.attachment_type.JSON)
        return response


    @allure.step('Выполнить запрос на создание задачи, забрав task_id')
    def get_id_created_task(self, task_data):
        response = requests.post(self.tasks_user_url, json=task_data, headers=self.headers)
        print(response.json())
        task_id = response.json()['data'].get('id')
        return task_id

    def update_task(self, task_id, update_data):
        """Обновляет задачу"""
        url = f"{self.tasks_user_url}/{task_id}"
        response = requests.put(url, json=update_data, headers=self.headers)
        return response


    @allure.step('Выполнить запрос на удаление задачи по task_id')
    def delete_task(self, task_id):
        url = f"{self.tasks_url}/{task_id}"
        response = requests.delete(url, headers=self.headers)

        with allure.step("Лог: url"):
            allure.attach(body=response.request.url, name='Request URL')
        with allure.step("Лог: статус код и тело ответа"):
            allure.attach(body=str(response.status_code), name='Status Code',
                          attachment_type=allure.attachment_type.JSON)
            allure.attach(body=response.text, name='Response Body', attachment_type=allure.attachment_type.JSON)
        return response