from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    
    order_feed_header = [By.XPATH, "//h1[text()='Лента заказов']"]

    order_number_window = [By.XPATH, "//p[text()='Ваш заказ начали готовить']"]


    order_number = [By.CSS_SELECTOR, "h2.text_type_digits-large"]

    close_button = [By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]"]

    completed_all_time = [By.XPATH, "//p[contains(@class, 'OrderFeed_number') and contains(@class, 'text_type_digits-large')]"]

    completed_today = [By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]"]

    orders_in_progress = [By.XPATH, "//li[contains(@class, 'text_type_digits')]"]

    loading_animation = [By.XPATH, "//img[@alt='loading animation']"]