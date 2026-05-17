import requests
import os           
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):
    api_key = os.getenv('API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        print(1212, weather,'kdkdkdkdkdk')
        return weather
    else:
        return None
    
if __name__ == "__main__":
    city = input("Enter city name: ")
    weather = get_weather(city)
    
    if weather:
        print(f"The weather we have now in {weather['city']} is simply: {weather['temperature']}°C, {weather['description']}")
    else:
        print("City not found.")