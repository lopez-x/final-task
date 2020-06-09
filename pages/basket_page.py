from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
#        self.browser.implicitly_wait(timeout)
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_BASKET), "Basket is not empty"

    def message_about_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "There is no message about empty basket"