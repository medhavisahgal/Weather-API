import requests
API_KEY = "418fe5f9aab51750af3618c0e4b2f538"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
city = input("Enter a city: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'], 2)
    feelslike = round(data['main']['feels_like'], 2)
    mintemp = round(data['main']['temp_min'], 2)
    maxtemp = round(data['main']['temp_max'], 2)
    humidity = data['main']['humidity']
    print("Weather: ", weather)
    print("Temperature: ", temperature, "C")
    print("Temperature feels like :", feelslike, "C")
    print("Minimum temperature: ", mintemp, "C")
    print("Maximum temperature: ", maxtemp, "C")
    print("Humidity: ", humidity, "%")
else:
    print("ERROR")
