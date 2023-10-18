import requests
import os
import sys


from ..message_discord.message_discord import DiscordMessenger

discord_webhook_url = os.environ['DISCORD_WEBHOOK_URL']

# Create an instance of DiscordMessenger
discord_messenger = DiscordMessenger(discord_webhook_url)


# Configuration
api_key = 'f7bb0829a3ba41678b921402231810'  # Replace with your OpenWeatherMap API key
location = 'grimstad'  # Replace with your desired location

# Fetch weather data
def fetch_weather_data():
    api_url = f'https://api.weatherapi.com/v1/current.json?q={location}&key={api_key}'
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
def send_notification(weather_data):
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

    discord_messenger.send_message(message_data)

# Main function
def main():
    try:
        weather_data = fetch_weather_data()
        send_notification(weather_data)
    except Exception as error:
        print('Error:', error)

if __name__ == '__main__':
    main()
