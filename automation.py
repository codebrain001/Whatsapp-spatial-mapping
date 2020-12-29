import time
from selenium import webdriver
chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://web.whatsapp.com/')

time.sleep(45)
print('Scanning the QR code completed')

# Finding the Whatsapp Group
group_name = 'PortHarcourt School of AI'
group = chrome_browser.find_element_by_class_name('_1MZWu')
print('About to click...')
group.click()


contacts = chrome_browser.find_element_by_xpath(
    '//*[@id="main"]/header/div[2]/div[2]/span')
print(contacts.get_attribute('textContent'))
