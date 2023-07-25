# Weather Forecast App

This is a simple Python program that interacts with the OpenWeatherMap API to fetch and display hourly weather forecast data for a specific location. The program provides the user with options to get weather details, wind speed, and pressure for a given date.

## Requirements

- Python 3.x
- `requests` library (You can install it using `pip install requests`)

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/your-username/weather-forecast-app.git
   cd weather-forecast-app
   ```

2. Run the program:
   ```
   python weather_app.py
   ```

3. Enter the city location (currently set to "London") and choose one of the following options:
   - 1: Get weather
   - 2: Get Wind Speed
   - 3: Get Pressure
   - 0: Exit

4. Depending on the option you choose, the program will prompt you for a date (in the format "YYYY-MM-DD") and display the corresponding weather data.

5. The program will continue running until you choose option "0" to exit.

## Screenshots

![25](https://github.com/atalnegi/assignment/assets/93611928/24b147d5-3131-470d-a33b-c51fa66f5e01)


## Disclaimer

This program uses the OpenWeatherMap API for weather forecast data. Please note that the provided API key is for testing purposes only and may have limitations on usage. It is recommended to use your own API key for extended usage or commercial purposes.

Happy forecasting! 🌤️
