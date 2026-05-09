from selenium.webdriver.common.by import By



REGISTRATION = {

"name_input": (By.XPATH, ".//fieldset[1]/div/div/input"), #поле ввода имени в форме регистрации

"email_input": (By.XPATH, ".//fieldset[2]/div/div/input"), # поле ввода почты в форме регистрации

"password_input": (By.NAME, "Пароль"), # поле ввода пароля в форме регистрации

"register_button": (By.XPATH, ".//button[text()='Зарегистрироваться']"), # кнопка Зарегистрироваться

"register_link": (By.XPATH, "//a[text()='Зарегистрироваться']"),

"incorrect_password_text": (By.XPATH, ".//p[text()='Некорректный пароль']"), # текст о некорректном пароле

"login_link": (By.LINK_TEXT, "Войти") # ссылка Войти

}

AUTH_LOC = {

"login_account_button": (By.XPATH, ".//button[text()='Войти в аккаунт']"), # кнопка войти в аккаунт

"email_field": (By.XPATH, ".//fieldset[1]/div/div/input"), #поле ввода почты

"password_field": (By.CSS_SELECTOR, "input[type='password'][name='Пароль']"), # поле ввода пароля

"entrance_button": (By.XPATH, ".//button[text()='Войти']"), # кнопка Войти


"recover_password_link": (By.LINK_TEXT, "Восстановить пароль"), # ссылка Восстановить пароль

"restore_button": (By.XPATH, ".//button[text()='Восстановить']"), # кнопка Восстановить в форме восстановления пароля

"entrance_link": (By.LINK_TEXT, "Войти") # ссылка Войти в форме восстановления пароля

}

ACCOUNT_PAGE = {

"place_an_order_button": (By.XPATH, ".//button[text()='Оформить заказ']"), # кнопка Оформить заказ

"personal_account": (By.CSS_SELECTOR, "a[href='/account']"), # кнопка Личный кабинет

}