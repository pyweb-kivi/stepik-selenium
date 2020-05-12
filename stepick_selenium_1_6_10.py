from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    url = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Firefox()
    browser.get(url)

    # Filling out fields
    first_name = browser.find_element_by_tag_name("input")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.CSS_SELECTOR, "input.second")
    last_name.send_keys("Petrov")
    email = browser.find_element_by_class_name("third")
    email.send_keys("tets@test.com")
    phone = browser.find_element_by_xpath("//label[text()='Phone:']/following-sibling::input")
    phone.send_keys("+777777777777")
    address = browser.find_element_by_xpath("//input[@placeholder='Input your address:']")
    address.send_keys("Russian, SP, Nevskiy av.")


    # Form submission
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
    