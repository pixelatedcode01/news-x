import requests
import os


class Weather:
    """ """

    def __init__(self, country):
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{country.replace(' ', '')}?unitGroup=metric&include=current&key=ZFRQGEWFMT86RPVYMWC6APD7T&contentType=json"
        response = requests.get(url)
        weather_json = response.json()
        weather = weather_json["days"]
        self.weather = weather

    def get_current_weather(self):
        """"""
        return self.weather[0]

    def get_weather_icon(self, icon):
        icons = os.listdir("icons")
        icons_with_labels = {}
        for item in icons:
            if item.split(".")[0] not in icons_with_labels:
                icons_with_labels[item.split(".")[0]] = item

        return f"icons/{icons_with_labels[icon]}"
