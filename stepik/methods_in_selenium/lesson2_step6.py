from selenium import webdriver
import time
import math

 # Вычисляем x по формуле
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element("id", "input_value").text
    y = calc(x)

    field = browser.find_element("xpath", "//input[@id='answer']")
    field.send_keys(y)

    robot_checkbox = browser.find_element("xpath", "//input[@id='robotCheckbox']")
    robot_checkbox.click()

    robot_radio = browser.find_element("xpath", "//input[@id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio)
    robot_radio.click()

    # Отправляем заполненную форму
    button = browser.find_element("xpath", "//button[text()='Submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()