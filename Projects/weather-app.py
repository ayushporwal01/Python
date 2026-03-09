import requests

city = input("Enter the name of a city: ")
key = "a43d4b64bede580d5c2ce6baab4e0db3"
url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={key}"

r = requests.get(url)
print(r.text)