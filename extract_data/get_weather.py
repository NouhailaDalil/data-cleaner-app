import time
import pandas as pd
import seaborn as sns 
import requests
import matplotlib as plt

API_KEY = "3ca0fea562a1f1b15910dbe1dd90bd95"
BASE_URL = "http://api.weatherstack.com/current"

 
def get_weather(city):
    params = {
        'access_key' : API_KEY,
        'query' : city
        } 
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if "current" in data:
            return {
        'city' : city,
        "temperature" : data["current"]["temperature"],
        "humidity" : data["current"]["humidity"],
        "wind_speed": data["current"]["wind_speed"],
        "feelslike" : data["current"]["feelslike"],
        "weather_descriptions": data["current"]["weather_descriptions"][0]
        }           
        else:
            print(f"Aucune donnée pour {city} : {data.get('error')}")
            return None   
    else:
        print(f"Erreur pour {city} : status code {response.status_code}")
        return None
    

