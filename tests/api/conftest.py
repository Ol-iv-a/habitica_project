import os

import pytest
from dotenv import load_dotenv

from pages.api.auth_page import AuthPage
from tests.resources.task_data import get_data


@pytest.fixture(scope="session")
def auth_headers():
    auth_page = AuthPage()
    load_dotenv()
    headers = auth_page.login_and_get_headers(os.getenv("USERNAME"), os.getenv("PASSWORD"))

    yield headers

@pytest.fixture(scope="function")
def tasks_page(auth_headers):
    from pages.api.task_page import TasksPage
    return TasksPage(auth_headers)


@pytest.fixture(scope="function")
def tasks_page_without_headers():
    from pages.api.task_page import TasksPage
    return TasksPage({"x-client": "habitica-web"})

@pytest.fixture(scope="function")
def test_task_id(tasks_page):
    task_id = tasks_page.get_id_created_task(get_data)

    yield task_id

    if task_id:
        tasks_page.delete_task(task_id)
