from selenium.webdriver.common.devtools.v133.fetch import continue_request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import math
import pytest

@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestParameters:
    def test_authorization(self, browser,lesson):
        link = f"https://stepik.org/lesson/{lesson}/step/1"
        browser.get(link)

        # Open authorization form
        enter_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(("xpath", "(//a[text()='Войти'])[1]"))
        )
        enter_button.click()

        # Entering email
        email_field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(("xpath", "//input[@id='id_login_email']"))
        )
        email_field.send_keys("<EMAIL>") # type email

        # Entering password
        password_field = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(("xpath", "//input[@id='id_login_password']"))
        )
        password_field.send_keys("<PASSWORD>") # type password

        # Submit button
        submit_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(("xpath", "//button[@type='submit']"))
        )
        submit_button.click()

        # Waiting for the page to reload
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(("xpath", "//img[@class='navbar__profile-img']"))
        )

        # log time for answer
        answer = math.log(int(time.time()))

        # Click 'again button' if textarea is not empty
        if len(browser.find_elements("xpath", "//textarea[@disabled]")) > 0:
            again_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable(("xpath", "//button[@class='again-btn white']"))
            )
            again_button.click()
            # Ожидание, пока textarea станет активной
            WebDriverWait(browser, 10).until_not(
                EC.presence_of_element_located(("xpath", "//textarea[@disabled]"))
            )

        # Explicitly waiting for the field to become visible and enter the answer in
        text_area = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(("xpath", "//textarea[@class='ember-text-area ember-view textarea string-quiz__textarea']"))
        )
        text_area.click()
        text_area.clear()
        text_area.send_keys(str(answer))

        # Click submit_button
        submit_button1 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(("xpath", "//button[text()='Отправить']"))
        )
        submit_button1.click()

        # Waiting for hint after the answer
        smart_hint = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(("xpath", "//p[@class='smart-hints__hint']"))
        )

        actual_text = smart_hint.text
        expected_text = "Correct!"
        assert actual_text == expected_text, f"Ожидался текст '{expected_text}', но получен '{actual_text}'"
