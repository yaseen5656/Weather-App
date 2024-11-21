from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

api_key = "ba0cc36b5574063ec4ea6be524f5d01d"  

def get_weather(city):
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        if not location:
            return {"error": "City not found"}

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")

        api = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={api_key}"
        response = requests.get(api)
        json_data = response.json()

        if json_data.get("cod") != 200:
            return {"error": json_data.get("message", "Invalid response")}

        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        return {
            "city": city,
            "time": current_time,
            "temp": f"{temp}°C",
            "condition": condition,
            "description": description,
            "pressure": pressure,
            "humidity": humidity,
            "wind": wind,
        }

    except Exception as e:
        return {"error": str(e)}
