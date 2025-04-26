from selenium import webdriver
import os
import time

from selenium.webdriver import Keys

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element("xpath", "//input[@name='firstname']")
    first_name = first_name.send_keys("Kirill")

    last_name = browser.find_element("xpath", "//input[@name='lastname']")
    last_name = last_name.send_keys("Terskikh")

    email = browser.find_element("xpath", "//input[@name='email']")
    email = email.send_keys("terkir@gmail.com")

    file = browser.find_element("xpath", "//input[@id='file']")
    current_directory = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_directory, "test.txt")
    file.send_keys(file_path)

    submit = browser.find_element("xpath", "//button[text()='Submit']")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
