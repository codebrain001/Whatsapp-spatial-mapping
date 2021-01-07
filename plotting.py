from decouple import config

import plotly.express as px
import chart_studio
from chart_studio import plotly as py

# Setting credentials
px.set_mapbox_access_token(config('mapbox_public_token'))
cs_username = config('chart_studio_username')
cs_api = config('chart_studio_api')
chart_studio.tools.set_credentials_file(username=cs_username,
                                        api_key=cs_api)


class SpatialMapping:

    def plot_map(self, dataframe):
        fig = px.scatter_mapbox(
            dataframe, lat="latitude", lon="longitude",
            color="counts",
            size="counts",
            color_continuous_scale=px.colors.sequential.Greens,
            size_max=20,
            zoom=1,
            hover_data=["country", 'counts'],
            hover_name='country')

        fig.update_layout(
            title='WhatsApp Analytics: Spatial Mapping of WhatsApp group contacts',
            mapbox_style="dark")

        fig.show()

        print('The link to the plot can be found here: ', py.plot(
            fig, filename='Whatsapp Analytics Map', auto_open=True))

    def plot_bar(self, dataframe):
        fig = px.bar(
            dataframe, x='country', y='counts',
            hover_data=["country", 'counts'],
            color_discrete_sequence=['darkgreen'])

        fig.update_layout(
            title='WhatsApp Analytics: Distribution of WhatsApp group contacts')
        fig.show()
