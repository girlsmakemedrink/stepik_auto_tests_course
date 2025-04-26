import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.execute_script("document.title='Script executing';alert('Robots at work');")

time.sleep(2)
