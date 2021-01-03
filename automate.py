import os
import time
import re
import csv
from selenium import webdriver


class WhatsappAutomation:
    def __init__(self):
        self.chrome_browser = webdriver.Chrome('./chromedriver')
        self.chrome_browser.maximize_window()
        self.chrome_browser.get('https://web.whatsapp.com/')
        time.sleep(30)

    def get_contacts(self, whatsapp_group_xpath, contact_element_xpath):
        group = self.chrome_browser.find_element_by_xpath(whatsapp_group_xpath)
        group.click()
        time.sleep(10)
        contacts = self.chrome_browser.find_elements_by_xpath(
            contact_element_xpath)
        # Note: The find elements returns a list object
        contacts = contacts[0].get_attribute('textContent')
        # print(contacts_content)
        # print(type(contacts_content))
        # We have to remove white spaces in the numbers
        contacts = re.sub(r"\s+", "", contacts)
        # We have to remove stmbols such as '()-'
        contacts = re.sub(r"[()-]+", "", contacts)
        # Your number is shown as 'You' on whatsapp Group, we have to remove that also
        contacts = contacts.replace(",You", "")

        # convert the string to list
        contact_list = contacts.split(',')
        # writing the contacts (list) to a csv file
        f = open('contact_data.csv', 'w')
        w = csv.writer(f, delimiter=',', )
        # create header
        w.writerow(['contact'])
        # split the common separated string values into a CSV file
        w.writerows([x.split(',') for x in contact_list])
        f.close()
        return contact_list

    def quit(self):
        print('Quiting session in 10 seconds...')
        time.sleep(10)
        self.chrome_browser.quit()
