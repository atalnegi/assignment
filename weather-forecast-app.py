import requests

API_BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"
API_KEY = "b6907d289e10d714a6e88b30761fae22"

def get_weather_data(city):
    url = f"{API_BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data.")
        return None


def get_temperature(data, date):
    for forecast in data["list"]:
        if forecast["dt_txt"].split()[0] == date:
            return forecast["main"]["temp"]
    return None


def get_wind_speed(data, date):
    for forecast in data["list"]:
        if forecast["dt_txt"].split()[0] == date:
            return forecast["wind"]["speed"]
    return None


def get_pressure(data, date):
    for forecast in data["list"]:
        if forecast["dt_txt"].split()[0] == date:
            return forecast["main"]["pressure"]
    return None


def main():
    city = "London"
    weather_data = get_weather_data(city)

    if weather_data is None:
        return

    while True:
        print("1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Terminating the program.")
            break
        elif choice == 1:
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_temperature(weather_data, date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature} °C")
            else:
                print("Weather data not found for the given date.")
        elif choice == 2:
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed(weather_data, date)
            if wind_speed is not None:
                print(f"Wind speed on {date}: {wind_speed} m/s")
            else:
                print("Weather data not found for the given date.")
        elif choice == 3:
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Weather data not found for the given date.")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
