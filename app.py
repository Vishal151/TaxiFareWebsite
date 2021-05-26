import streamlit as st
from datetime import datetime, date
import numpy as np
import pandas as pd
import requests
import params

st.sidebar.markdown('# TaxiFare in NY 🗽')
pickup_date = st.sidebar.date_input("When do you want to take a taxi?", value=datetime(2012, 10, 6, 12, 10, 20))
pickup_time = st.sidebar.time_input("When exactly?", value=datetime(2012, 10, 6, 12, 10, 20))
pickup = st.sidebar.text_input("Departure", 'Empire State Building')
dropoff = st.sidebar.text_input("Arrival", 'JFK Airport')
passenger_count = st.sidebar.number_input('passenger_count', min_value=1, max_value=8, step=1, value=1)

st.markdown('''
  # TaxiFareModel in NY 🗽
''')

if st.sidebar.button('Get Fare'):
  pickup_datetime = f'{pickup_date} {pickup_time}'
  pickup_url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{pickup}.json?'
  dropoff_url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{dropoff}.json?'
  mbparams = {'access_token': params.mbtoken,
              'bbox': '-74.109308,40.560583,-73.618356,40.953794',
              'limit': 2}
  pickup_latitude, pickup_longitude = requests.get(
      pickup_url, params=mbparams).json()['features'][0]['center']
  dropoff_latitude, dropoff_longitude = requests.get(
      dropoff_url, params=mbparams).json()['features'][0]['center']

  params = dict(
      pickup_datetime=pickup_datetime,
      pickup_longitude=pickup_longitude,
      pickup_latitude=pickup_latitude,
      dropoff_longitude=dropoff_longitude,
      dropoff_latitude=dropoff_latitude,
      passenger_count=passenger_count
  )
  
  url = 'https://taxifare.lewagon.ai/predict'

  response = requests.get(url, params=params).json()

  pred = round(response['prediction'], 2)
  st.write(f"You're gonna pay ${pred} 💸. Take an UBER")
  st.image('https://s23527.pcdn.co/wp-content/uploads/2015/03/955a95136c9cdd5bce9438aef49453ab.gif')

mycomment = '''
2. Let's build a dictionary containing the parameters for our API...
3. Let's call our API using the `requests` package...
4. Let's retrieve the prediction from the **JSON** returned by the API...
## Finally, we can display the prediction to the user
'''

