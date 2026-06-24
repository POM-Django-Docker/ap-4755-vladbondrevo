from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/auth/login/")
        self.driver.maximize_window()


    def test_valid_login_and_logout(self):

        driver = self.driver

        # Find login fields
        email = driver.find_element(By.ID, "id_email")
        password = driver.find_element(By.ID, "id_password")

        # Enter valid credentials
        email.send_keys("admin@gmail.com")
        password.send_keys("admin123")

        # Submit form
        password.send_keys(Keys.RETURN)

        time.sleep(2)

        # Verify successful login
        self.assertIn(
            "dashboard",
            driver.current_url
        )


        # Logout
        driver.get("http://127.0.0.1:8000/auth/logout/")

        time.sleep(2)


        # Verify logout
        self.assertIn(
            "login",
            driver.current_url
        )



    def test_invalid_login(self):

        driver = self.driver

        email = driver.find_element(By.ID, "id_email")
        password = driver.find_element(By.ID, "id_password")

        email.send_keys("wrong@gmail.com")
        password.send_keys("wrongpassword")

        password.send_keys(Keys.RETURN)

        time.sleep(2)

        self.assertIn(
            "невірний email або пароль",
            driver.page_source.lower()
        )



    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()
