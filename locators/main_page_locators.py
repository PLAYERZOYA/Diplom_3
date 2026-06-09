from selenium.webdriver.common.by import By

class MainPageLocators:

    constructor_button = (By.XPATH, "//p[text()='Конструктор']")

    constructor_title = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")

    ingredient_counter = (By.CLASS_NAME, "counter_counter__num__3nue1")

    order_feed_button = (By.XPATH, "//p[text()='Лента Заказов']")

    basket_container = [By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket')]"]

    order_button =  (By.XPATH, "//button[text()='Оформить заказ']")

    INGREDIENTS = {

    "fluorescent_bun": (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")

    }
  

    CONTENT_BOX = {

    "modal_content_box": (By.XPATH, "//img[@alt='tick animation']"), # всплывающее окно с деталями об ингредиенте

    "close_modal_button": (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]") # крестик для закрытия окна

    }

    

   