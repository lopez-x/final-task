from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.product_page import ProductPage
import time
import pytest

xfile = 7
mask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
links = [mask+str(i) for i in range(10) if i != xfile]
xlink = pytest.param(mask+str(xfile), marks=pytest.mark.xfail(reason="mistake on page"))
links.insert(xfile, xlink)

@pytest.mark.parametrize('link', links)
def test_quiz_and_get_code(browser, link):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
    time.sleep(5)
