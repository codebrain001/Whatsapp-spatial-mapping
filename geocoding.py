from decouple import config
import pandas as pd 
import googlemaps 

class GoogleGeocoding:
    def __init__(self):
        self.key = config('api_key')
        self.gmaps = googlemaps.Client(key=self.key)

    def geocode_df(self, dataframe):
        print('Preparing for geocoding...')
        df = dataframe
        df = df.value_counts().rename_axis('country').reset_index(name='counts')
        for index in df.index:
            df.loc[index, 'longitude'] = (self.gmaps.geocode(df['country'][index]))[0].get('geometry').get('location').get('lng')
            df.loc[index, 'latitude'] = (self.gmaps.geocode(df['country'][index]))[0].get('geometry').get('location').get('lat')
        df.to_csv('geocode_data.csv', index=False)
        print('Geocoding completed')
        return df

