from selenium import webdriver
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import time
import pytest

#xfile = 7
#mask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
#links = [mask+str(i) for i in range(10) if i != xfile]
#xlink = pytest.param(mask+str(xfile), marks=pytest.mark.xfail(reason="mistake on page"))
#links.insert(xfile, xlink)

#@pytest.mark.parametrize('link', links)
#def test_quiz_and_get_code(browser, link):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#    page = ProductPage(browser, link)
#    page.open()
#    page.press_button_add_to_basket()
#    page.solve_quiz_and_get_code()
#    page.should_be_message_about_adding()
#    page.should_be_message_basket_total()
#    time.sleep(5)

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
#    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
#    page.solve_quiz_and_get_code()
    page.should_dissapear_of_success_message()
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

