from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.XPATH, "//span/a[contains(@class, 'btn')][contains(@href, 'basket')]")
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//div/a[contains(@class, 'btn')][contains(@href, 'checkout')]")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


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
