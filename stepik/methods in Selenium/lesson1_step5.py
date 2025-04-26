from selenium import webdriver
import time
import math

 # Вычисляем x по формуле
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим x
    x_element = browser.find_element("xpath", "//span[@id='input_value']")
    x = x_element.text
    print(x)
    y = calc(x)

    field = browser.find_element("xpath", "//input[@id='answer']")
    field.send_keys(y)

    robot_checkbox = browser.find_element("xpath", "//input[@id='robotCheckbox']")
    robot_checkbox.click()

    robot_radio = browser.find_element("xpath", "//input[@id='robotsRule']")
    robot_radio.click()

    # Отправляем заполненную форму
    button = browser.find_element("xpath", "//button[text()='Submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()