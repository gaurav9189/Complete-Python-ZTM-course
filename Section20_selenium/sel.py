from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('chromedriver')

chrome_browser = webdriver.Chrome(service=service)

chrome_browser.maximize_window()
chrome_browser.get('http://demo.seleniumeasy.com/basic-first-form-demo.html')

# Using the class name to get the text on the first button from the list
button_element_byclass = chrome_browser.find_elements(
    By.CLASS_NAME, 'btn-default')
button_text = button_element_byclass[0].text

# Using the CSS selector printing the text on buttons(there were 2)
button_element = chrome_browser.find_elements(By.CSS_SELECTOR, '.btn-default')
for button in button_element:
    button.text  # can print to show other buttons

# Here > represents any button child of the id type get-input
button_element_bycss = chrome_browser.find_elements(
    By.CSS_SELECTOR, '#get-input > .btn-default')

print(f'The button element by class is: {button_element_bycss}')

# This will error if not true. page source searches the entire html page
assert 'Show Message' in chrome_browser.page_source


input_message = chrome_browser.find_elements(By.ID, 'user-message')
input_message[0].clear()
input_message[0].send_keys('I Am so cool?')
button_element[0].click()

output_message = chrome_browser.find_elements(By.ID, 'display')
print(f'The output of what you entered was: {output_message[0].text}')
assert 'I Am so cool?' in output_message[0].text
print('All done!')
while True:
    pass
