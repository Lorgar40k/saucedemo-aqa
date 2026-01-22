# Saucedemo AQA Project

Автоматизация тестирования веб-приложения [Sauce Demo](https://www.saucedemo.com/).

Технологии: Python 3.11, Pytest, Selenium WebDriver, Page Object Pattern, Allure Reports, Docker, Webdriver Manager.

В проекте реализовано 5 основных тестов для авторизации: успешный логин стандартным пользователем, логин с неверным паролем, логин заблокированного пользователя, логин с пустыми полями, логин пользователя performance_glitch_user. Все тесты используют Page Object Pattern.

Запуск локально (Windows): создать виртуальное окружение командой `python -m venv venv`, активировать `venv\Scripts\activate`, установить зависимости `pip install -r requirements.txt`, запустить тесты `pytest`, просмотреть Allure отчет `allure serve allure-results`.

Запуск через Docker: собрать образ `docker compose build`, запустить контейнер `docker compose run --rm tests`, просмотреть Allure отчет `allure serve ./allure-results`.

Структура проекта:

saucedemo-aqa/
|
|-- tests/           # Тесты
|   `-- test_login.py
|
|-- pages/           # Page Object
|   `-- login_page.py
|
|-- requirements.txt
|-- Dockerfile
|-- docker-compose.yml
|-- pytest.ini
`-- README.md




Тест-кейсы:

1. **Успешный логин стандартным пользователем**  
   Открыть страницу логина, ввести логин `standard_user` и пароль `secret_sauce`, нажать кнопку входа.  
   Ожидаемый результат: переход на страницу inventory и отображение товаров.

2. **Логин с неверным паролем**  
   Ввести логин `standard_user` и неверный пароль `wrong_password`, нажать кнопку входа.  
   Ожидаемый результат: отображение ошибки о неверном пароле.

3. **Логин заблокированного пользователя**  
   Ввести логин `locked_out_user` и пароль `secret_sauce`, нажать кнопку входа.  
   Ожидаемый результат: отображение ошибки о заблокированном пользователе.

4. **Логин с пустыми полями**  
   Не вводить логин и пароль, нажать кнопку входа.  
   Ожидаемый результат: отображение ошибки о пустых полях.

5. **Логин пользователя performance_glitch_user**  
   Ввести логин `performance_glitch_user` и пароль `secret_sauce`, нажать кнопку входа.  
   Ожидаемый результат: переход на страницу inventory и отображение товаров, возможно с задержкой.

Все тесты используют Page Object Pattern для разделения логики взаимодействия с веб-страницей и тестов.
