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
![gif](./overview-1.gif)
![gif](./overview-2.gif)

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