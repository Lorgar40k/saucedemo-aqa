from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def open_login_page(self):
        self.open(self.URL)

    def login(self, username="", password=""):
        self.find(self.USERNAME).send_keys(username)
        self.find(self.PASSWORD).send_keys(password)
        self.click(self.LOGIN_BUTTON)

    def is_error_displayed(self):
        return self.find(self.ERROR_MESSAGE).is_displayed()

    def is_inventory_page_opened(self):
        return self.find(self.INVENTORY_CONTAINER).is_displayed()
