# import nexmo
# from pprint import pprint

# client = nexmo.Client(key='31a8b23d', secret='XLu6QzbdWFuvEyyy')

# insight_json = client.get_advanced_number_insight(number='2348141921557')
# pprint(insight_json)

import geocoder
g = geocoder.google('Nigeria')
print(g.latlng)
