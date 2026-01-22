import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")           # Headless режим для Docker
    options.add_argument("--no-sandbox")         # Требуется в Linux/Docker
    options.add_argument("--disable-dev-shm-usage")  # Избегаем проблем с памятью
    options.add_argument("--window-size=1920,1080")

    # Используем ChromeDriver, установленный в контейнере
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()


@allure.title("Успешный логин стандартным пользователем")
def test_successful_login(driver):
    page = LoginPage(driver)
    page.open_login_page()
    page.login("standard_user", "secret_sauce")

    assert "inventory.html" in page.get_current_url()
    assert page.is_inventory_page_opened()


@allure.title("Логин с неверным паролем")
def test_login_with_wrong_password(driver):
    page = LoginPage(driver)
    page.open_login_page()
    page.login("standard_user", "wrong_password")

    assert page.is_error_displayed()


@allure.title("Логин заблокированного пользователя")
def test_locked_out_user(driver):
    page = LoginPage(driver)
    page.open_login_page()
    page.login("locked_out_user", "secret_sauce")

    assert page.is_error_displayed()


@allure.title("Логин с пустыми полями")
def test_login_with_empty_fields(driver):
    page = LoginPage(driver)
    page.open_login_page()
    page.login()

    assert page.is_error_displayed()


@allure.title("Логин performance_glitch_user")
def test_performance_glitch_user(driver):
    page = LoginPage(driver)
    page.open_login_page()
    page.login("performance_glitch_user", "secret_sauce")

    assert "inventory.html" in page.get_current_url()
    assert page.is_inventory_page_opened()
