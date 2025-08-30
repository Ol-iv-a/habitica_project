import allure
from selene import browser, have

from selene.support.conditions.be import visible


class TasksPage:
    def __init__(self):
        self.create_button = browser.element('.create-task-area')
        self.add_habit = browser.all('.dropdown-item.d-flex.px-2.py-1').element(0)
        self.add_daily_routine = browser.all('.dropdown-item.d-flex.px-2.py-1').element(1)
        self.add_task = browser.all('.dropdown-item.d-flex.px-2.py-1').element(2)

        self.habit_list = browser.all('.tasks-list').element(0)
        self.daily_routine_list = browser.all('.tasks-list').element(1)
        self.task_list = browser.all('.type_todo')
        self.list = browser.all('.task-item')



        self.quick_add_habit = browser.element('placeholder="Добавить привычку"')
        self.quick_add_daily_routine = browser.element('placeholder="Добавить ежедневное дело"')
        self.quick_task = browser.element('placeholder="Добавить задачу"')

        self.task_modal_heading = browser.element('.my-auto.task-purple-modal-headings')
        self.fill_name = browser.element('[placeholder="Добавить название"]')
        self.checklist = browser.element('placeholder="Новый пункт списка"')
        self.save_button = browser.element('.btn.btn-secondary.d-flex.align-items-center.justify-content-center')
        self.cancel_button = browser.element('.cancel-task-btn')
        self.delete_button = browser.element('.delete-task-btn')

    @allure.step('Создать задачу')
    def create_task(self, name):
        self.create_button.click()
        self.add_task.click()
        self.fill_name.set_value(name)
        self.save_button.click()

    @allure.step('Быстрое добавление задачи')
    def quick_create_task(self):
        self.quick_task.set_value('задача тест').press_enter()

    @allure.step('Отредактировать задачу')
    def update_task(self, old_name, new_name):
        self.task_list.element_by(have.text(old_name)).click()
        self.fill_name.set_value(new_name)
        self.save_button.click()

    @allure.step('Удалить задачу')
    def delete_task(self, name):
        self.task_list.element_by(have.text(name)).click()
        self.delete_button.click()

        alert = browser.driver.switch_to.alert
        alert_text = alert.text
        print(f'Текст окна: {alert_text}')
        alert.accept()  # Нажимаем "ОК"

    @allure.step('Проверить обновление задачи')
    def check_update_task(self, name):
        self.task_list.element_by(have.text(name)).should(visible)

    @allure.step('Проверить удаление задачи')
    def check_delete_task(self, name):
        self.list.should(have.size(0))
