import unittest
from selenium import webdriver

link1 = "https://suninjuly.github.io/registration1.html"
link2 = "https://suninjuly.github.io/registration2.html"

class TestAbs(unittest.TestCase):

    def test_link1(self):

         try:
            browser = webdriver.Chrome()
            browser.get(link1)

            first_name = browser.find_elements("xpath", "//input[@placeholder='Input your first name']")
            self.assertTrue(len(first_name) > 0, f"Элемент first_name отсутствует")

            first_name[0].send_keys("Stepik")

            last_name = browser.find_elements("xpath", "//input[@placeholder='Input your last name']")
            self.assertTrue(len(last_name) > 0, f"Элемент last_name отсутствует")

            last_name[0].send_keys("Stepikov")

            email = browser.find_elements("xpath", "//input[@placeholder='Input your email']")
            self.assertTrue(len(email) > 0, f"Элемент email отсутствует")

            email[0].send_keys("Stepik@Stepikov.org")
         finally:
             browser.quit()

    def test_link2(self):

         try:
            browser = webdriver.Chrome()
            browser.get(link2)

            first_name = browser.find_elements("xpath", "//input[@placeholder='Input your first name']")
            self.assertTrue(len(first_name) > 0, f"Элемент first_name отсутствует")

            first_name[0].send_keys("Stepik")

            last_name = browser.find_elements("xpath", "//input[@placeholder='Input your last name']")
            self.assertTrue(len(last_name) > 0, f"Элемент last_name отсутствует")

            last_name[0].send_keys("Stepikov")

            email = browser.find_elements("xpath", "//input[@placeholder='Input your email']")
            self.assertTrue(len(email) > 0, f"Элемент email отсутствует")

            email[0].send_keys("Stepik@Stepikov.org")
         finally:
             browser.quit()

if __name__ == "__main__":
    unittest.main()