import requests

city = input("Enter the name of a city: ")
key = "50965f50b67b56afdf33799237c592a6"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"

r = requests.get(url)
print(r.text)