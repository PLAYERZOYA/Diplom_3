import allure
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedPageLocators()

    @allure.step("Проверка видимости заголовка 'Лента заказов'")
    def is_order_feed_header_visible(self):
        return self.wait_for_element_visible(self.locators.order_feed_header).is_displayed()

    @allure.step("Получение значения счётчика 'Выполнено за всё время'")
    def get_completed_all_time(self):
        element = self.wait_for_element_visible(self.locators.completed_all_time)
        return int(element.text)

    @allure.step("Получение значения счётчика 'Выполнено за сегодня'")
    def get_completed_today(self):
        element = self.wait_for_element_visible(self.locators.completed_today)
        return int(element.text)

    @allure.step("Получение номера заказа в разделе В работе")
    def get_first_order_in_progress(self):
        element = self.wait_for_element_visible(self.locators.orders_in_progress)
        return element.text