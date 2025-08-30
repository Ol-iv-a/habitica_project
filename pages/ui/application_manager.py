from pages.ui.home_page import HomePage
from pages.ui.login_page import LoginPage
from pages.ui.tasks_page import TasksPage


class ApplicationManager():
    def __init__(self):
        self.home_page = HomePage()
        self.login_page = LoginPage()
        self.tasks_page = TasksPage()

