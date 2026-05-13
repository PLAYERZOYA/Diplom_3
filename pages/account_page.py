import allure
from selenium.webdriver.common.by import By
from locators.account_page_locators import REGISTRATION, AUTH_LOC, ACCOUNT_PAGE
from pages.base_page import BasePage
from data.data import Urls


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.registration_locators = REGISTRATION
        self.auth_locators = AUTH_LOC
        self.account_locators = ACCOUNT_PAGE
        self.urls = Urls()

    @allure.step("Клик на кнопку Личный кабинет")
    def click_personal_account(self):
 
        self.wait_for_element_visible(self.account_locators["personal_account"])
      
        self.click_element_with_wait_clickable(self.account_locators["personal_account"])
       

    @allure.step("Клик на ссылку Зарегистрироваться")
    def click_register_link(self):
        self.click_element_with_wait_clickable(self.registration_locators["register_link"])

    @allure.step("Заполнение формы регистрации")
    def fill_registration_form(self, name, email, password):
        self.wait_for_element_visible(self.registration_locators["name_input"])
        self.fill_field(self.registration_locators["name_input"], name)
        self.fill_field(self.registration_locators["email_input"], email)
        self.fill_field(self.registration_locators["password_input"], password)
        self.click_element_with_wait_clickable(self.registration_locators["register_button"])

    @allure.step("Полная регистрация нового пользователя")
    def register_new_user(self, name, email, password):
       
        self.driver.get(self.urls.main_page_url)

        self.click_personal_account()

        
        self.click_register_link()
        self.fill_registration_form(name, email, password)

    @allure.step("Авторизация пользователя")
    def login(self, email, password):
        self.wait_for_element_clickable(self.auth_locators["entrance_button"])
        self.fill_field(self.auth_locators["email_field"], email)
        self.fill_field(self.auth_locators["password_field"], password)
        self.click_element_with_wait_clickable(self.auth_locators["entrance_button"])
        self.wait_for_element_visible(self.account_locators["place_an_order_button"]).is_displayed()

    @allure.step("Регистрация и авторизация")
    def register_and_login(self, name, email, password):
 
        self.register_new_user(name, email, password)
        self.wait_for_element_visible(self.auth_locators["email_field"])
        self.login(email, password)
