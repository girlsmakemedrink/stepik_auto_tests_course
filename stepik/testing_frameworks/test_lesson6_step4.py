import math
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest

link = "https://stepik.org/lesson/236895/step/1"

def test_authorization(browser):
    browser.delete_all_cookies()
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    enter_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(("xpath", "//a[@id='ember466']"))
    )
    enter_button.click()

    email_field = browser.find_element("xpath", "//input[@id='id_login_email']")
    email_field.send_keys("<EMAIL>") # type email

    password_field = browser.find_element("xpath", "//input[@id='id_login_password']")
    password_field.send_keys("<PASSWORD>") # type password

    submit_button = browser.find_element("xpath", "//button[@type='submit']")
    submit_button.click()

    with pytest.raises(NoSuchElementException):
        browser.find_element("xpath", "//input[@id='ember542']")

    answer = math.log(int(time.time()))
    print(answer)
    time.sleep(5)