from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestSuiteOfRegistrationFlow(unittest.TestCase):

    def setUp (self):
        
         self.browser = webdriver.Chrome()

    def tearDown (self):
         self.browser.quit () 

    # the first test suite to verify the second loging flow 
    def test_first_flow_of_registration(self):   
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)

        input_firstName = self.browser.find_element (By.XPATH, '//div[@class="first_block"]//input[@class="form-control first"]')
        input_firstName.send_keys ("First_name_test")
        input_lastName = self.browser.find_element (By.XPATH, '//div[@class="first_block"]//input[@class="form-control second"]')
        input_lastName.send_keys ("Last_name_test")
        input_email = self.browser.find_element (By.XPATH, '//div[@class="first_block"]//input[@class="form-control third"]')
        input_email.send_keys ("stepick@test.com")
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "PASSED")


    # the second test suite to verify the second loging flow 
    def test_second_flow_of_registration(self):
            link = "http://suninjuly.github.io/registration1.html"
            self.browser.get(link)

            input_firstName = self.browser.find_element (By.XPATH, '//div[@class="first_block"]//input[@class="form-control first"]')
            input_firstName.send_keys ("First_name_test")
            input_lastName = self.browser.find_element (By.XPATH, '//div[@class="first_block"]//input[@class="form-control second"]')
            input_lastName.send_keys ("Last_name_test")
            input_email = self.browser.find_element (By.XPATH, '//div[@class="irst_block"]//input[@class="form-control third"]')
            input_email.send_keys ("stepick@test.com")
            button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "PASSED")

if __name__ == "__main__":
    unittest.main()