import requests
from pytemp import pytemp #docs located at https://pypi.org/project/pytemp/ by zainraza
from dotenv import load_dotenv
import os


def weather_status_container(): #set weather info into a container 
    weather_data_collection = {"city_temp_statement" : "Unknown",
    "humidity_statement" : "Unknown", "wind_speed" : "Unknown", "city_name" : "Unknown",
    "state_name" : "Unknown", "country_name" : "Unknown"}

    if geo_latitude != "Unknown" or geo_longitude != "Unknown":
        city_temp = round(pytemp(weather_info["main"]["temp"],"k","f"))
        city_temp_statement = "{} F".format(city_temp)
        weather_data_collection["city_temp_statement"] = city_temp_statement
        weather_data_collection["humidity_statement"] = "Humidity: {} %".format(weather_info["main"]["humidity"])
        weather_data_collection["wind_speed"] = "{} m/s".format(weather_info["wind"]["speed"])
        weather_data_collection["city_name"] = geo_info[0]["name"]
        weather_data_collection["state_name"] = geo_info[0]["state"]
        weather_data_collection["country_name"] = geo_info[0]["country"]
    return weather_data_collection    

load_dotenv()
api_key = os.getenv("api_key")
if not api_key:
    raise ValueError("No API Key found")

geolocator_url = "http://api.openweathermap.org/geo/1.0/direct?"
relevant_city_name = input()
geo_url_address =  "{0}q={1}&limit=1&appid={2}".format(geolocator_url,relevant_city_name,api_key)
geo_request = requests.get(geo_url_address)
geo_info = geo_request.json()


if geo_info:
    geo_latitude = geo_info[0]["lat"]
    geo_longitude = geo_info[0]["lon"]
else:
    geo_latitude = "Unknown"
    geo_longitude = "Unknown"


weather_data_url = "https://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&appid={2}".format(geo_latitude,geo_longitude,api_key)
weather_request = requests.get(weather_data_url)
weather_info = weather_request.json()
print(weather_status_container())
