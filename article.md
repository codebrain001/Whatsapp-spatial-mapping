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

**N/B:** It is good practice to add the `.env` file to the [gitignore]('https://git-scm.com/docs/gitignore') file. This prevent sensitive information such as API keys and other configuration values to be made public on the source code.

To access these environment variable values, we can utilize an already install python library [Python Decouple]('https://pypi.org/project/python-decouple/').

## Overview of the project

## Scripts and explanation