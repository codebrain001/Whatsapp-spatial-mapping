# Whatsapp Analytics: Spatial mapping of users of whatsapp groups 

In this tutorial, we are going to build an interface that aids the geocoding of WhatsApp users in a group chat to have spatial insights and understanding of the collective conversations in Whatsapp groups. This system will be built with python using Selenium, Plotly, Vonage Number Insight API, Google Map API, and Mapbox API.

## Prerequisites
In order to follow and fully understand this tutorial, you'll need to have:
- [Python 3.6](https://www.python.org/) or newer.
- Basic knowledge of automation with [selenium]('https://selenium-python.readthedocs.io/index.html)
- Set up [Vonage API]('https://www.vonage.com/') account
- Set up [Google Map API]('https://developers.google.com/maps/documentation')
- Set up [Plotly]('https://plotly.com/') and [Mapbox]('https://www.mapbox.com/') credentials

Below are the result of the final interface you’ll build:
![gif](./images/overview-1.gif)
![gif](./images/overview-2.gif)

## File Structure
An overview of the file directory for this project, which has been arranged to enforce clean coding best practices is shown below:
├── README.md
├── analytics.py
├── automate.py
├── chromedriver
├── env
├── geocoding.py
├── main.py
└── plotting.py

We will create all the files in the above directory tree through the steps of this tutorial.

## Set up a Python Virtual Environment

We need to create an isolated environment for various Python dependencies unique to this project.

First, create a new development folder. In your terminal, run:

```
mkdir whatsapp-spatial-mapping
```
Next, create a new Python virtual environment. If you are using Anaconda, you can run the following command:

```
conda create -n env python=3.6
```
Then you can activate the environment using:

```
conda activate env
```

If you are using a standard distribution of Python, create a new virtual environment by running the command below:

```
python -m venv env
```

To activate the new environment on a Mac or Linux computer, run:

```
source env/bin/activate
```

If you are using a Windows computer, activate the environment as follows:

```
venv\Scripts\activate
```

Regardless of the method you used to create and activate the virtual environment, your prompt should have been modified to look like the following:

```
(whatsapp-spatial-mapping) $
```

### Requirement file
Next with your virtual environment set up, we will install the project dependencies and their specific version (These dependencies versions were the current versions at the time of writing this article)

```
chart-studio==1.1.0
googlemaps==4.4.2
nexmo==2.5.2
numpy==1.19.4
pandas==1.2.0
plotly==4.14.1
plotly-express==0.4.1
python-decouple==3.3
selenium==3.141.0
```

You can simply `$ pip install -r requirements.txt` or `conda install --file requirements.txt` (if you are on Anaconda) and voila! All of the program’s “dependencies” will be downloaded, installed, and ready to go in one fell swoop.

Optionally, you can install all the packages as follows:

- Using Pip:
  ```
    pip install chart-studio googlemaps nexmo numpy pandas plotly plotly-express python-decouple selenium
  ```
- Using Conda:
  ```
    conda install -c conda-forge chart-studio googlemaps nexmo numpy pandas plotly plotly-express python-decouple selenium
  ```

## Setting up APIs and Credentials
With all our dependencies completed installed for this tutorial, we need to set up some accounts to get our API keys and credentials.

### Vonage API Account
To complete this tutorial, you will need a [Vonage API account]('https://dashboard.nexmo.com/sign-in'). If you don’t have one already, you can [sign up today]('https://dashboard.nexmo.com/sign-up') and start building with free credit. Once you have an account, you can find your API Key and API Secret at the top of the [Vonage API Dashboard]('https://dashboard.nexmo.com/sign-in').

### Google Map Platform 
The Google Map API is one of the potent APIs readily available on [Google Cloud Console]('https://console.cloud.google.com/'). Firstly, you need to set up a [Google cloud free tier account]('https://cloud.google.com/free'), where you get $300 free credits to explore the Google cloud platform and products.  Next, with Your Google Cloud Console all set up, you need to [create an API]('https://developers.google.com/maps/documentation/javascript/get-api-key') key to connect the [Google Map Platform]('https://cloud.google.com/maps-platform') to our application. Lastly, we [activate the Google Map API ]('https://cloud.google.com/service-usage/docs/enable-disable') to enable it for our project.

### Plotly API and Mapbox Credentials
In order to create beautiful data visualizations, we will be utilizing [Plotly]('https://plotly.com/') on Python and enhancing the aesthetic with [Mapbox]('https://www.mapbox.com/'). The Plotly plots is hosted online on Chart Studio (part of Plotly enterprise), you need to [sign up]('https://chart-studio.plotly.com/Auth/login/#/') and generate and save our custom [Plotly API key]('https://plotly.com/python/getting-started-with-chart-studio/'). Also beneficial to the desired plots, you need to [sign up at Mapbox]('https://account.mapbox.com/auth/signup/'). Next, to connect Mapbox with Plotly for our desired visualization, we need to create a [Mapbox authorization token]('https://docs.mapbox.com/help/tutorials/get-started-tokens-api/').

## Separation of settings parameters and source code
In the previous section, we were actively generating various API keys and credentials which are variables that exist outside of our source code and are unique to each user. 
Firstly you need to create an environment file (.env), which can easily be done on your IDE by creating a new file and naming it `.env` or can be done via the terminal as follow:
```
(whatsapp-spatial-mapping) $ touch .env   # create a new .env file
(whatsapp-spatial-mapping) $ nano .env    # open the .env file 
```
 An environment variable is made up of a name/value pair, and any number may be created and available for reference at a point in time.

 For example, the content of the `.env` file should look somewhat like this:
 ```
    user=Brain
    key=xxxxxxxxxxxxxxxxxxxxxxxxxx
 ```

Parameters related to the project, goes straight to the source code. Parameters related to an instance of the project, goes to an environment file. 

**Note:** It is good practice to add the `.env` file to the [gitignore]('https://git-scm.com/docs/gitignore') file. This prevent sensitive information such as API keys and other configuration values to be made public on the source code.

To access these environment variable values, we can utilize an already install python library [Python Decouple]('https://pypi.org/project/python-decouple/').

## Project scope statement
According to WhatsApp statistics, more than 2 billion people in over [180 countries in 60 languages]('https://www.whatsapp.com/about/') uses WhatsApp. WhatsApp, however, remains a market leader in the social media sector with it features of voice and video calling, group calls and has moves into the payment market for business with the launch of WhatsApp business in 2018.

WhatsApp groups has served as environment to establish collective conversations with others around the world. These groups are effective when established for specific reasons so topics discussed and shared are aligned to the purpose of the group. 

For a business use case, it might be interesting to know where users are located to deliver better services and products better. This tutorial is a step in the right direction to aid this analytic procedure and build an interface to geo-locate users in a WhatsApp group.

## Scripts and explanation
Each script is written to contain codes that handle or work together to achieve a common goal utilizing the Object-Oriented Programming paradigm. The following are a high-level explanation for each script.

1. automate.py
To make this project seamless, we are going to do a bit of automation, Whatsapp automation to be precise.  Selenium is an open-source web-based automation tool, we have already installed it in the installation section. Selenium requires a driver to interface with the browser, and they are different drivers for different browsers. Links to some popular browsers drivers are found below: 
   - Chrome driver can be downloaded [here]('https://sites.google.com/a/chromium.org/chromedriver/downloads').
   - Firefox driver can be downloaded [here]('https://github.com/mozilla/geckodriver/releases').
   - Safari driver can be downloaded [here]('https://webkit.org/blog/6900/webdriver-support-in-safari-10/').
   - Edge driver can be downloaded [here]('https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/').
   
**Note:** In this project, I used the chrome driver. To make the path of the driver quickly and simple to access, move the downloaded driver file to the same directory of the script utilizing it. Take a look at the file structure above.

This script is made up of a `WhatsappAutomation` class that loads the web driver via it's path, maximize the browser window and loads Whatsapp Web application. The 30s delay initiated is to enable the scanning of the QR code 

   

***
```
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
        # We have to remove white spaces in the numbers
        contacts = re.sub(r"\s+", "", contacts)
        # We have to remove stmbols such as '()-'
        contacts = re.sub(r"[()+-]", "", contacts)
        # Your number is shown as 'You' on whatsapp Group, we have to remove that also
        contacts = contacts.replace(",You", "")

        # convert the string to list
        contact_list = contacts.split(',')
        # writing the contacts (list) to a csv file
        f = open('contact_data.csv', 'w')
        w = csv.writer(f, delimiter=',')
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
```


   1. geocoding.py

```
from decouple import config
import pandas as pd 
import googlemaps 

class GoogleGeocoding:
    def __init__(self):
        self.key = config('api_key')
        self.gmaps = googlemaps.Client(key=self.key)

    def geocode_df(self, dataframe):
        print('Preparing for geocoding country code...')
        df = dataframe
        df = df.value_counts().rename_axis('country').reset_index(name='counts')
        for index in df.index:
            df.loc[index, 'longitude'] = (self.gmaps.geocode(df['country'][index]))[0].get('geometry').get('location').get('lng')
            df.loc[index, 'latitude'] = (self.gmaps.geocode(df['country'][index]))[0].get('geometry').get('location').get('lat')
        df.to_csv('geocode_data.csv', index=False)
        print('Geocoding completed')
        return df
```

3. plotting.py

```
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
```

4. main.py
   
```
from automate import WhatsappAutomation
from analytics import WhatsappAnalytics
from geocoding import GoogleGeocoding
from plotting import SpatialMapping

if __name__ == '__main__':

    automated_object = WhatsappAutomation()
    group_xpath = '//*[@id="pane-side"]/div[1]/div/div'
    contact_xpath = '//*[@id="main"]/header/div[2]/div[2]/span'
    contact_list = automated_object.get_contacts(group_xpath, contact_xpath)
    automated_object.quit()

    analytics_object = WhatsappAnalytics()
    analytics_df = analytics_object.get_insights(contact_list)

    geocoding_object = GoogleGeocoding()
    geo_df = geocoding_object.geocode_df(analytics_df)

    spatial_mapping_object = SpatialMapping()
    spatial_mapping_object.plot_map(geo_df)
    spatial_mapping_object.plot_bar(geo_df)
```


## Results 