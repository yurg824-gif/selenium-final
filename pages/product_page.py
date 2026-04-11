from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    
    def  should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_PRODUCT_BUTTON), "Add button is not presented"

    def add_product_to_basket(self):
        # Получить наименование и цену товара
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        add_button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
        add_button.click()

    def should_be_product_in_basket(self):
        msg = self.browser.find_element(*ProductPageLocators.MSG_PRODUCT_IN_BASKET)
        msg_expected_text = self.product_name + " был добавлен в вашу корзину."        
        assert msg.text == msg_expected_text, "There is no message about adding the item to the cart"
        pass        

    def should_be_basket_cost_eq_product(self):
        msg_basket_cost = self.browser.find_element(*ProductPageLocators.MSG_BASKET_COST)
        msg_expected_basket_cost = "Всего в корзине: " + self.product_price + "\nПосмотреть корзину"        
        assert msg_basket_cost.text == msg_expected_basket_cost, "The basket value is not equal to the product price"
        pass