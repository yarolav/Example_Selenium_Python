from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try: 
    browser.get("http://suninjuly.github.io/wait2.html")
    browser = webdriver.Chrome()
    # to tell Selenium is checking while 5-seconds until the button is becoming clickable 
    button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "verify")))
    button.click ()
    message = browser.find_element (By.ID, "verify_message")
    print (message)

    assert "successful" in message.text
    print (message)
    
finally:
    # add delay in the execution of a program
    time.sleep (10)
    # to close chrome and kill procces 
    browser.quit ()