import time
import pandas as pd
from get_weather import get_weather

df_villes = pd.read_csv("data/villes_maroc.csv")
weather_data = []

def weather_dataset():
    for ville in df_villes['name']:
        try:
            meteo = get_weather(ville)
            time.sleep(1) 
            if meteo is not None and 'code' not in meteo:               
                weather_data.append(meteo)         
        except Exception as e:
            print(f"Erreur pour la ville {ville} : {e}")
weather_dataset()
df_weather = pd.DataFrame(weather_data)
df_weather.to_csv("data/weather_dataset.csv", index=False)
