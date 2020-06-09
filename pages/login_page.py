from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
#        driver.current_url# реализуйте проверку на корректный url адрес
        assert self.browser.current_url, "Login link is not found"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        input1 = self.browser.find_element(*BasePageLocators.EMAIL_REG)
        input1.send_keys(email)
        input2 = self.browser.find_element(*BasePageLocators.PASSWORD_REG) 
        input2.send_keys(password)
        input3 = self.browser.find_element(*BasePageLocators.PASSWORD_REPEAT) 
        input3.send_keys(password)
        input4 = self.browser.find_element(*BasePageLocators.REG_BUTTON)
        input4.click()