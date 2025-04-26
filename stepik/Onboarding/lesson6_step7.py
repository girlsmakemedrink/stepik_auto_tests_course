from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

try:
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements("xpath", "//input[@type='text']")
    for element in elements:
        element.send_keys("1")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла