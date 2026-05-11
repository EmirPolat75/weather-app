import requests

city = input("Enter city name: ")

api_key = "YOUR_API_KEY"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data = response.json()

if response.status_code == 200:
    print("\nWeather Information")
    print("-------------------")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["description"])

else:
    print("City not found or API error.")
