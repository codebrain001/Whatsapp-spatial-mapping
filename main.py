from automate import WhatsappAutomation
from analytics import WhatsappAnalytics
from geocoding import GoogleGeocoding
from plotting import SpatialMapping


def main()


if __name__ == '__main__':

    automated_object = WhatsappAutomation()
    group_xpath = '//*[@id="pane-side"]/div[1]/div/div'
    contact_xpath = '//*[@id="main"]/header/div[2]/div[2]/span'
    contact_list = automated_object.get_contacts(
        group_xpath, contact_xpath)
    automated_object.quit()

    analytics_object = WhatsappAnalytics()
    analytics_df = analytics_object.get_insights(contact_list)

    geocoding_object = GoogleGeocoding()
    geo_df = geocoding_object.geocode_df(analytics_df)

    spatial_mapping_object = SpatialMapping()
    spatial_mapping_object.plot_map(geo_df)
    spatial_mapping_object.plot_bar(geo_df)


main()
