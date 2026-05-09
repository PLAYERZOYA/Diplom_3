import pytest
from selenium import webdriver
from data.data import Urls
from pages.account_page import AccountPage
from pages.main_page import MainPage

import random



@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    
    driver.get(Urls.main_page_url)

    yield driver
    driver.quit()


# генерация почты и пароля 
@pytest.fixture
def generate_email_and_password():
    name = random.choice(['test', 'user', 'student', 'coder'])
    surname = random.choice(['testov', 'userov', 'studentov', 'coderov'])
    cohort = random.randint(10, 99)
    digits = random.randint(100, 999)

    email = f"{name}_{surname}_{cohort}_{digits}@ya.ru"
    
    password = str(random.randint(100000, 999999))

    return email, password

@pytest.fixture
def registered_user(driver, generate_email_and_password):
    email, password = generate_email_and_password
    name = "TestUser"
    account_page = AccountPage(driver)

    account_page.register_and_login(name, email, password)

    return email, password


@pytest.fixture
def created_order(driver, registered_user):
    email, password = registered_user
    main_page = MainPage(driver)
    main_page.create_order()
    main_page.wait_for_order_window()
    order_number = main_page.get_order_number()
    main_page.close_order_window()
    return order_number