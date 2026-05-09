import allure
from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage
from data.data import Urls


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()
        self.order_feed_locators = OrderFeedPageLocators()
        self.urls = Urls()

    @allure.step("Клик на кнопку Конструктор")
    def click_constructor_button(self):
        self.click_element_with_wait_clickable(self.locators.constructor_button)

    @allure.step("Клик на кнопку Лента заказов")
    def click_order_feed_button(self):

        self.click_element_with_wait_clickable(self.locators.order_feed_button)
        self.wait_for_element_visible(self.order_feed_locators.order_feed_header)
        
    @allure.step("Клик на ингредиент")
    def click_ingredient(self):
        ingredient_locator = self.locators.INGREDIENTS["fluorescent_bun"]
        self.wait_for_element_clickable(ingredient_locator)
        self.click_element_with_wait_clickable(ingredient_locator)

    @allure.step("Закрытие всплывающего окна кликом по крестику")
    def close_modal(self):
        
        self.wait_for_element_clickable(self.locators.CONTENT_BOX["close_modal_button"])
        self.click_element(self.locators.CONTENT_BOX["close_modal_button"])
        self.wait_for_element_invisible(self.locators.CONTENT_BOX["modal_content_box"])

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_to_order(self):
        ingredient_locator = self.locators.INGREDIENTS["fluorescent_bun"]
        self.wait_for_element_visible(ingredient_locator)
        self.wait_for_element_visible(self.locators.basket_container)
        

        self.drag_and_drop(ingredient_locator, self.locators.basket_container)


    @allure.step("Получение значения счётчика ингредиента")
    def get_ingredient_counter(self):
        element = self.wait_for_element_visible(self.locators.ingredient_counter)
        return element.text
    

    @allure.step("Создание заказа")
    def create_order(self):
        ingredient_locator = self.locators.INGREDIENTS["fluorescent_bun"]
        self.drag_and_drop(ingredient_locator, self.locators.basket_container)

        self.click_element_with_wait_clickable(self.locators.order_button)

    @allure.step("Ожидание появления окна с номером заказа")
    def wait_for_order_window(self):
        self.wait_for_element_visible(self.order_feed_locators.loading_animation)
        self.wait_for_element_invisible(self.order_feed_locators.loading_animation)
        self.wait_for_element_visible(self.order_feed_locators.order_number_window)
        self.wait_for_element_visible(self.order_feed_locators.close_button)

    @allure.step("Получение номера заказа из всплывающего окна")
    def get_order_number(self):
        element = self.wait_for_element_visible(self.order_feed_locators.order_number)
        return element.text
        import time
        time.sleep(2)

    @allure.step("Закрытие всплывающего окна с номером заказа")
    def close_order_window(self):
        self.click_element_with_wait_clickable(self.order_feed_locators.close_button)
        self.wait_for_element_invisible(self.order_feed_locators.order_number_window)
        self.wait_for_element_clickable(self.locators.order_feed_button)
        import time
        time.sleep(2)


    @allure.step("Переход в Ленту заказов")
    def go_to_order_feed_page(self):
        self.wait_for_element_clickable(self.locators.order_feed_button)
        self.click_order_feed_button()