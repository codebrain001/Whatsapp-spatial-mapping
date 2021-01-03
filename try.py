import nexmo
import json
from pprint import pprint

client = nexmo.Client(key='31a8b23d', secret='XLu6QzbdWFuvEyyy')

contacts = ['2348099899375', '2348141921557']
data = '{}'
data_json = json.loads(data)
with open('data.json', 'w') as file:
    for contact in contacts:
        insight_json = client.get_advanced_number_insight(number=contact)
        data_json.update(insight_json)
        file.seek(0)
        json.dump(data_json, file)



#     with open('test.json', 'r+') as file:
#         data = json.load(file)
#         insight_json = client.get_advanced_number_insight(number=contact)
#         data.update(insight_json)
#         file.seek(0)
#         json.dump(data,file)

# pprint(insight_json)

# import geocoder
# g = geocoder.google('Nigeria')
# print(g.latlng)

# Psuedo code workflow

# Set up all the enivronment variables

# Get random sample of the data

# Geo encode: Geocoder

# Set up Mapbox

# Plot the spatial map
