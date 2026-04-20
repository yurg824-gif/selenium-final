from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert 'login' in self.browser.current_url, "Ссылка на страницы входа(Login url) некорректна"

    def should_be_login_form(self):
        #  проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма входа (Login form) отсутствует"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации (Register form) отсутствует"

    def register_new_user(self, email:str, password:str):
        register_email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        register_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        register_confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_FIELD)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_email_field.send_keys(email)
        register_password_field.send_keys(password)
        register_confirm_password_field.send_keys(password)
        register_button.click()        