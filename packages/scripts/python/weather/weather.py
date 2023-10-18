import requests

class WeatherNotifier:
    def __init__(self, discord_messenger):
        self.discord_messenger = discord_messenger

    # Configuration
    api_key = 'f7bb0829a3ba41678b921402231810'  # Replace with your OpenWeatherMap API key
    location = 'grimstad'  # Replace with your desired location

    # Fetch weather data
    def fetch_weather_data(self):
        api_url = f'https://api.weatherapi.com/v1/current.json?q={self.location}&key={self.api_key}'
        try:
            response = requests.get(api_url)
            if response.status_code != 200:
                raise Exception('Unable to fetch weather data')
            data = response.json()
            return data
        except Exception as error:
            print('Error:', error)
            return None

    # Send a notification
    def send_notification(self, weather_data):
        if not weather_data:
            return

        current = weather_data['current']
        temperature = current['temp_c']
        weather_description = current['condition']['text']
        feels_like = current['feelslike_c']

        message = f'Temperature: {temperature}°C\nConditions: {weather_description}. but it feels like {feels_like}°C'

        message_data = {
            "title": "Weather in Grimstad",
            "custom_message": message,
            "user": "Weather Bot",
            "avatar_url": current['condition']['icon'],
            "html_url": "https://www.valiantlynx.com",
        }

        self.discord_messenger.send_message(message_data)

    # Main function
    def main(self):
        try:
            weather_data = self.fetch_weather_data()
            self.send_notification(weather_data)
        except Exception as error:
            print('Error:', error)

