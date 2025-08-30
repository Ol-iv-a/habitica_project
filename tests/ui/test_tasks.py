import allure
from pages.ui.application_manager import ApplicationManager


@allure.feature("Задачи")
@allure.title("Создание задачи")
@allure.description("Проверяем успешное создание задачи")
@allure.tag("UI", 'SUCCESS')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://habitica.com/", name="Website")
def test_create_tack():
    app = ApplicationManager()
    app.home_page.go_to_login()
    app.login_page.login_with_email('firpo@powerscrews.com', '0a+qPV4a')
    app.tasks_page.create_task('задача')
    app.tasks_page.check_update_task('задача')


@allure.feature("Задачи")
@allure.title("Редактирование задачи")
@allure.description("Проверяем успешное редактирование задачи")
@allure.tag("UI", 'SUCCESS')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://habitica.com/", name="Website")
def test_update_tack():
    app = ApplicationManager()
    app.home_page.go_to_login()
    app.login_page.login_with_email('firpo@powerscrews.com', '0a+qPV4a')
    app.tasks_page.update_task('задача','задача_1')
    app.tasks_page.check_update_task('задача_1')


@allure.feature("Задачи")
@allure.title("Удаление задачи")
@allure.description("Проверяем успешное удаление задачи")
@allure.tag("UI", 'SUCCESS')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://habitica.com/", name="Website")
def test_delete_task():
    app = ApplicationManager()
    app.home_page.go_to_login()
    app.login_page.login_with_email('firpo@powerscrews.com', '0a+qPV4a')
    app.tasks_page.delete_task('задача_1')
    app.tasks_page.check_delete_task('задача_1')