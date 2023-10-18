import argparse
from weather.weather import WeatherNotifier
from message_discord.message_discord import DiscordMessenger
import os

def weather_discord_message():
    if __name__ == '__main__':
        discord_webhook_url = os.environ['DISCORD_WEBHOOK_URL']
        discord_messenger = DiscordMessenger(discord_webhook_url)

        weather_notifier = WeatherNotifier(discord_messenger)
        weather_notifier.main()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run specific functions')
    parser.add_argument('function_name', choices=['weather_discord_message'], help='Name of the function to run')

    args = parser.parse_args()

    if args.function_name == 'weather_discord_message':
        weather_discord_message()
    
