import os
import allure
from jsonschema import validate
from pages.model import schemas
from tests.resources.task_data import get_data

@allure.feature("Задачи")
@allure.title("Получение списка задач авторизованным пользователем")
@allure.description("Проверяем успешное получение списка задач авторизованным пользователем")
@allure.tag("API", 'SUCCESS')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(os.getenv('BASE_URL') + os.getenv('TASKS_USER_ENDPOINT'))
def test_get_user_tasks(tasks_page):
    r = tasks_page.get_user_tasks()
    with allure.step('Проверить, что статус код = 200'):
        assert r.status_code == 200
    with allure.step('Проверить, что ответ соответствует схеме'):
        validate(r.json(), schema=schemas.get_tasks)
    with allure.step('Проверить, что задачи авторизованного пользователя'):
        data = r.json()
        for task in data['data']:
            assert task['userId'] == r.request.headers.get('x-api-user')


@allure.feature("Задачи")
@allure.title("Получение списка задач неавторизованным пользователем")
@allure.description("Проверяем ошибку при получение списка задач неавторизованным пользователем")
@allure.tag("API", 'FAILED')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(os.getenv('BASE_URL') + os.getenv('TASKS_USER_ENDPOINT'))
def test_get_user_tasks_unauthorized(tasks_page_without_headers):
    r = tasks_page_without_headers.get_user_tasks()
    with allure.step('Проверить, что статус код = 401'):
        assert r.status_code == 401
    with allure.step('Проверить текст ошибки'):
        assert r.json()['message'] == 'Missing authentication headers.'


@allure.feature("Задачи")
@allure.title("Получение списка задач по фильтру")
@allure.description("Проверяем успешное получение списка задач по фильтру авторизованным пользователем")
@allure.tag("API", 'SUCCESS')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(os.getenv('BASE_URL') + os.getenv('TASKS_USER_ENDPOINT'))
def test_get_user_tasks_with_type_filter(tasks_page):
    r = tasks_page.get_user_tasks_with_type_filter('todos')
    with allure.step('Проверить, что статус код = 200'):
        assert r.status_code == 200
    with allure.step('Проверить, что в списке только задачи с типом todo'):
        data = r.json()
        for task in data['data']:
            assert task['type'] == 'todo'


@allure.feature("Задачи")
@allure.title("Получение списка задач по id")
@allure.description("Проверяем успешное получение списка задач по id авторизованным пользователем")
@allure.tag("API", 'SUCCESS')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(os.getenv('BASE_URL') + os.getenv('TASKS_ENDPOINT'))
def test_get_user_task_by_id(test_task_id, tasks_page):
    r = tasks_page.get_user_task_by_id(test_task_id)

    with allure.step('Проверить, что статус код = 200'):
        assert r.status_code == 200
    with allure.step('Проверить, что в списке только задачи с id'):
        assert r.json()['data']['id'] == test_task_id
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
