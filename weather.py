#import modules
import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass


load_dotenv() #load environment variables, API key here
api_key = os.getenv('API_KEY') #fetch API key for weather 


@dataclass
class WeatherData:
    #main: str
    icon: str
    temperature: float
    pressure: float
    humidity: float

def get_lat_lon(city_name, state_code, country_code, API_key):
    ''' Fetches longitude and latitude of the city using a Geocoding API call'''
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&&appid={API_key}"
    resp = requests.get(url).json()
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon


def get_current_weather(lat, lon, API_key):
    '''Makes an API call to fetch weather details and saves the required information'''
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"
    resp = requests.get(url).json()
    #main = resp.get('weather')[0].get('main')
    data = WeatherData(
        icon = resp.get('weather')[0].get('icon'),
        temperature = resp.get('main').get('temp'),
        humidity = resp.get('main').get('humidity'),
        pressure = resp.get('main').get('pressure')
    )
    return data


def main(city_name, state_name, country_name):
    lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data

if __name__ == "__main__":
    lat, lon = get_lat_lon('Miami', '', '', api_key)
    print(get_current_weather(lat, lon, api_key)) #sanity check