from automate import WhatsappAutomation

automated_object = WhatsappAutomation()
group_xpath = '//*[@id="pane-side"]/div[1]/div/div'
contact_xpath = '//*[@id="main"]/header/div[2]/div[2]/span'
contact_list = automated_object.get_contacts(group_xpath, contact_xpath)
automated_object.quit()




