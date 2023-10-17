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
import sys

discord_webhook_url = os.environ['DISCORD_WEBHOOK_URL']

# Create an instance of DiscordMessenger
discord_messenger = DiscordMessenger(discord_webhook_url)

# Check if a custom message was provided as a command-line argument
if len(sys.argv) > 1:
    custom_message = sys.argv[1]
    issue_type = sys.argv[2]
else:
    custom_message = "No custom message provided."


# Send a message to Discord
if issue_type == 'error':
    discord_messenger.send_error(custom_message)
elif issue_type == 'warning':
    discord_messenger.send_warning(custom_message)
elif issue_type == 'info':
    discord_messenger.send_info(custom_message)
else:
    discord_messenger.send_message(custom_message)
    
    

