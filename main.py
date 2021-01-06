from automate import WhatsappAutomation
from analytics import WhatsappAnalytics

automated_object = WhatsappAutomation()
group_xpath = '//*[@id="pane-side"]/div[1]/div/div'
contact_xpath = '//*[@id="main"]/header/div[2]/div[2]/span'
contact_list = automated_object.get_contacts(group_xpath, contact_xpath)
automated_object.quit()


analytics_object = WhatsappAnalytics()
analytics_object.get_insights(contact_list[0:10])
