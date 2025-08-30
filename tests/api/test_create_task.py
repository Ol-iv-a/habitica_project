import os
import allure
from jsonschema import validate
from pages.model import schemas
from tests.resources.task_data import get_data


@allure.feature("Задачи")
@allure.title("Создание задачи авторизованным пользователем")
@allure.description("Проверяем успешное создание задачи авторизованным пользователем")
@allure.tag("API", 'SUCCESS')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(os.getenv('BASE_URL')+ os.getenv('TASKS_USER_ENDPOINT'))
def test_create_task(tasks_page):
    r = tasks_page.create_task(get_data)
    with allure.step('Проверить, что статус код = 201'):
        assert r.status_code == 201
    with allure.step('Проверить, что ответ соответствует схеме'):
        validate(r.json(), schema = schemas.get_create_task)
    with allure.step('Проверить, что данные соответствуют созданному заданию'):
        task = r.json()['data']
        assert task['text'] == get_data['text']
        assert task['type'] == get_data['type']
        assert task['notes'] == get_data['notes']
        assert task['tags'] == get_data['tags']
        assert task['priority'] == get_data['priority']
    with allure.step('Проверить, что чеклист сохранен в правильном порядке'):
        assert len(task['checklist']) == len(get_data['checklist'])
        assert task['checklist'][0]['text'] == get_data['checklist'][0]['text']
        assert task['checklist'][1]['text'] == get_data['checklist'][1]['text']

    tasks_page.delete_task(task['id'])

@allure.feature("Задачи")
@allure.title("Создание задачи неавторизованным пользователем")
@allure.description("Проверяем ошибку при создании задачи неавторизованным пользователем")
@allure.tag("API", 'FAILED')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(os.getenv('BASE_URL')+ os.getenv('TASKS_USER_ENDPOINT'))
def test_create_task_unauthorized(tasks_page_without_headers):
    r = tasks_page_without_headers.create_task(get_data)
    print(r.json())
    with allure.step('Проверить, что статус код = 401'):
        assert r.status_code == 401
    with allure.step('Проверить текст ошибки'):
        assert r.json()['message'] == 'Missing authentication headers.'