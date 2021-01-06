from decouple import config
import json
import csv
import nexmo


class WhatsappAnalytics:
    def __init__(self):
        # Setting up Nexmo credentials
        self.key = config('client_key')
        self.secret = config('client_secret')
        self.client = nexmo.Client(key=self.key, secret=self.secret)

    def get_insights(self, contact_list):
        data = []
        for contact in contact_list:
            insight_json = self.client.get_advanced_number_insight(
            number=contact).get('country_name')
            data.append(insight_json)
       
        #convert the list
        f = open('country_data.csv', 'w')
        w = csv.writer(f, delimiter=',', )
         # create header
        w.writerow(['country'])
        # split the common separated string values into a CSV file
        w.writerows([x.split(' ') for x in data])
        f.close()
        # return data
       






       
        # # Saving the JSON file to memory
        # with open('Whatsapp_insights.json', 'w') as insight_json_file:
        #     json.dump(insight_json, insight_json_file)
        # return insight_json

