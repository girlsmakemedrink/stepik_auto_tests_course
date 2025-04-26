import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/redirect_accept.html")
    first_window = browser.window_handles[0]

    button = browser.find_element("xpath", "//button[text()='I want to go on a magical journey!']")
    button.click()
    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element("id", "input_value").text
    y = calc(x)

    answer_field = browser.find_element("id", "answer")
    answer_field.send_keys(y)

    submit = browser.find_element("xpath", "//button[text()='Submit']")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()