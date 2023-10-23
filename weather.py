import requests
import os


class Weather:
    """Class for retrieving and managing weather information."""

    def __init__(self, country):
        # Initialize the Weather object and retrieve weather data for a specific country
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{country}?unitGroup=metric&include=current&key=ZFRQGEWFMT86RPVYMWC6APD7T&contentType=json"
        response = requests.get(url)
        weather_json = response.json()
        weather = weather_json["days"]
        self.weather = weather

    def get_current_weather(self):
        # Retrieve the current weather data
        return self.weather[0]

    def get_weather_icon(self, icon):
        # Get the path to the weather icon based on the icon's filename
        icons = os.listdir("icons")
        icons_with_labels = {}
        for item in icons:
            if item.split(".")[0] not in icons_with_labels:
                icons_with_labels[item.split(".")[0]] = item

        return f"icons/{icons_with_labels[icon]}"
