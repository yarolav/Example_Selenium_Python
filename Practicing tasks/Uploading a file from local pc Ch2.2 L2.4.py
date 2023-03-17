from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html" 
    browser = webdriver.Chrome()
    browser.get(link)
    input_first_name = browser.find_element (By. CSS_SELECTOR, '[name="firstname"]').send_keys ('Ya_Test')
    input_last_name = browser.find_element (By. CSS_SELECTOR, '[name="lastname"]').send_keys ('B_Test')
    input_email = browser.find_element (By. CSS_SELECTOR, '[name="email"]').send_keys ('mm@mm.com')
    current_dir = os.path.abspath (os.path.dirname(__file__))
    file_name = "text_example.txt"
    file_path = os.path.join (current_dir, file_name)
    element = browser.find_element (By. CSS_SELECTOR, '[type="file"]').send_keys (file_path)
    button = browser.find_element (By. CSS_SELECTOR, '[type="submit"]').click ()

finally:
    # add delay in the execution of a program
    time.sleep (10)
    # to close chrome and kill procces 
    browser.quit ()
