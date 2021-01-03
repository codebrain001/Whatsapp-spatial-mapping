from decouple import config
import json
import nexmo


class WhatsappAnalytics:
    def __init__(self):
        # Setting up Nexmo credentials
        self.key = config('client_key')
        self.secret = config('client_secret')
        self.client = nexmo.Client(key=self.key, secret=self.secret)

    def get_insights(self, contact_list):
        insight_json = self.client.get_advanced_number_insight(
            number=contact_list)
        # Saving the JSON file to memory
        with open('Whatsapp_insights.json', 'w') as insight_json_file:
            json.dump(insight_json, insight_json_file)
        return insight_json

