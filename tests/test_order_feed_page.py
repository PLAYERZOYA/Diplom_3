import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("При создании нового заказа счетчик 'Выполнено за все время' увеличивается")
    def test_completed_all_time_counter_increases(self, driver, registered_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        
        main_page.go_to_order_feed_page()
        
        counter_before_order = order_feed_page.get_completed_all_time()
        
        # Создаём заказ
        driver.get(main_page.urls.main_page_url)
        main_page.create_order()
        main_page.wait_for_order_window()
        main_page.close_order_window()
        

        main_page.go_to_order_feed_page()
        counter_after_order = order_feed_page.get_completed_all_time()
        
        assert counter_after_order > counter_before_order


    @allure.title("При создании нового заказа счетчик Выполнено за сегодня увеличивается")
    def test_completed_today_counter_increases(self, driver, registered_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.go_to_order_feed_page()
        counter_before_order = order_feed_page.get_completed_today()
        
        driver.get(main_page.urls.main_page_url)
        main_page.create_order()
        main_page.wait_for_order_window()
        main_page.close_order_window()
        
        main_page.go_to_order_feed_page()
        counter_after_order = order_feed_page.get_completed_today()
        
        assert counter_after_order > counter_before_order


    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_order_number_appears_in_progress(self, driver, registered_user, created_order):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        order_number = created_order
        
        main_page.go_to_order_feed_page()
        order_in_progress = order_feed_page.get_first_order_in_progress()
        
        assert order_number in order_in_progress