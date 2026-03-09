import requests
from pyttsx3 import speak

city = input("Enter the name of a city: ")
key = "a43d4b64bede580d5c2ce6baab4e0db3"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"

data = requests.get(url).json()

temp = data["main"]["temp"]

print("temperature is ", temp, "°C")

speak(f"The current weather of {city} is {temp} °C")