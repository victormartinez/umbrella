from decouple import config


OPEN_WEATHER_HOST = "https://api.openweathermap.org"
OPEN_WEATHER_API_KEY = config("OPEN_WEATHER_API_KEY")
