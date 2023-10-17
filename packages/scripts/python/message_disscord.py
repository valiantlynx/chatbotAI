import requests
import datetime

class DiscordMessenger:
    def __init__(self, discord_webhook_url):
        self.discord_webhook_url = discord_webhook_url

    def send_message(self, message, color=0x00ff00):
        self._send_to_discord(message, color)

    def send_error(self, message):
        self._send_to_discord(message, 0xff0000)

    def send_warning(self, message):
        self._send_to_discord(message, 0xffff00)

    def send_info(self, message):
        self._send_to_discord(message, 0x0000ff)

    def _send_to_discord(self, message, color):
        embed = {
            "title": "Github Action",
            "description": message,
            "color": color,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "footer": {"text": "Github Action"},
        }
        payload = {"embeds": [embed]}
        response = requests.post(self.discord_webhook_url, json=payload)
        if response.status_code == 204:
            print('Message sent to discord.')
        else:
            print('Error sending message to discord.')
            print(response.status_code)
            print(response.text)


import os

discord_webhook_url = os.environ['DISCORD_WEBHOOK_URL']

# Create an instance of DiscordMessenger
discord_messenger = DiscordMessenger(discord_webhook_url)

# Use its methods to send messages
discord_messenger.send_message("This is an info message.")
discord_messenger.send_error("This is an error message.")
discord_messenger.send_warning("This is a warning message.")
discord_messenger.send_info("This is another info message.")
