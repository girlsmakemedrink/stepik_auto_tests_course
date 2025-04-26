import math
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("https://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element(("xpath", "//h5[@id='price']"), "$100")
    )
button = browser.find_element("xpath", "//button[@id='book']")
button.click()

x = browser.find_element("id", "input_value").text
y = calc(x)

answer_field = browser.find_element("id", "answer")
answer_field.send_keys(y)

submit = browser.find_element("xpath", "//button[text()='Submit']")
submit.click()

time.sleep(3)