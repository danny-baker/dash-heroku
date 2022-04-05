# dash-heroku
A starter pack for deploying a Plotly Dash app on Heroku

## Instructions

A full step-by-step guide is provided below to help you get your first Heroku app live. 
If you are a first-timer on Heroku, I suggest you get this starter app running on Heroku first, then you can adapt it to suite by copy-paste your Dash app code across etc.

## 1. Clone this repo to your local machine and install modules

It's a good idea to check you can get this app running on your local webserver before attempting to deploy on Heroku. So let's do that.
Setup your virtualenv (or don't) and ensure you have all the modules installed before running the app.

You should be able to do this with pip3 or conda install from a terminal in your project root folder

`pip3 install -r requirements.txt` or `conda install --file requirements.txt` (if you are using Anaconda)

## 2. Test the app locally

Run the app from your IDE direct, or like a boss from the terminal: `python3 app.py`

If it runs, it should be visible on a browser via `https://0.0.0.0:8050`

## 3. Setup Heroku command-line-interface (CLI)

Depending on your OS, you may also need to install Git. Follow the instructions on their website [here](https://devcenter.heroku.com/articles/heroku-cli).

## 4. Create a Heroku account

You will also need a Heroku account (free tier is fine for a hobby app). Sign up [here](https://signup.heroku.com/login).