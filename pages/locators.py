from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
    ADD_BTN = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    EMAIL_REG =(By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REG = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REPEAT = (By.ID, "id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > a")
    PRODUCT_BASKET = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#messages")