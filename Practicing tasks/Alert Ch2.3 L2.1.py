from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/alert_accept.html" 
    browser = webdriver.Chrome ()
    browser.get (link)
    journey_button = browser.find_element (By. TAG_NAME, 'button').click ()
    confirm = browser.switch_to.alert
    confirm.accept ()
    def calc (x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element (By.ID, "input_value")
    x = x_element.text
    y = calc (x)
    input_answer = browser.find_element (By.ID, "answer").send_keys (y)
    submit_button = browser.find_element (By. TAG_NAME, "button").click ()

finally:
    # add delay in the execution of a program
    time.sleep (10)
    # to close chrome and kill procces 
    browser.quit ()
