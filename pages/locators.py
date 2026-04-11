from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form > button")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    MSG_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    MSG_BASKET_COST = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
