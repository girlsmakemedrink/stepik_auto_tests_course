import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element("id", "num1")
    num2 = browser.find_element("id", "num2")
    sum = int(num1.text) + int(num2.text)

    select = Select(browser.find_element("tag name", "select"))

    select.select_by_visible_text(str(sum))

    # Отправляем заполненную форму
    button = browser.find_element("xpath", "//button[text()='Submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
