import requests

def get_weather(city):
    api_key = "08ed1a05b5efd14fdc18ff8bc833143e"
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"Weather Forecast for {data['city']['name']}:")
        # Group forecasts by date (show one entry per day)
        forecasts = {}
        for forecast in data['list']:
            date = forecast['dt_txt'].split()[0]  # Extract date part
            if date not in forecasts:
                forecasts[date] = {
                    'temp': forecast['main']['temp'],
                    'description': forecast['weather'][0]['description']
                }
        # Display forecast for each day
        for date, info in forecasts.items():
            print(f"Date: {date}")
            print(f"Temperature: {info['temp']}°C")
            print(f"Weather: {info['description'].capitalize()}\n")
    else:
        print("City not found. Please try again.")

city = input("Enter a city: ")        
get_weather(city)