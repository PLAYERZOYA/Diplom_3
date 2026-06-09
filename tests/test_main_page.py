import allure
from pages.main_page import MainPage


@allure.feature("Основная страница")
class TestMainPage:

    @allure.title("Переход по клику на кнопку Конструктор")
    def test_click_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor_button()
        assert driver.current_url == main_page.urls.main_page_url

    @allure.title("Переход по клику на кнопку Лента заказов")
    def test_click_order_feed_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        assert main_page.wait_for_element_visible(main_page.order_feed_locators.order_feed_header).is_displayed()

    @allure.title("При клике на ингредиент появляется всплывающее окно с деталями")
    def test_click_ingredient_modal_content_box_appears(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.wait_for_element_visible(main_page.locators.CONTENT_BOX["modal_content_box"]).is_displayed()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_modal_content_box_closes_by_cross(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.wait_for_element_visible(main_page.locators.CONTENT_BOX["modal_content_box"]).is_displayed()
        main_page.close_modal()
        assert main_page.wait_for_element_invisible(main_page.locators.CONTENT_BOX["modal_content_box"])

    @allure.title("При добавлении ингредиента в заказ счетчик увеличивается")
    def test_add_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.add_ingredient_to_order()
        assert main_page.get_ingredient_counter() == "2"