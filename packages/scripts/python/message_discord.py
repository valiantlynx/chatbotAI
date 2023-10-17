import requests
import datetime

class DiscordMessenger:
    def __init__(self, discord_webhook_url):
        self.discord_webhook_url = discord_webhook_url

    def send_message(self, message, color=0x00ff00, title=str, user=str, avatar_url=str, html_url=str):
        self._send_to_discord(message, color, title, user, avatar_url, html_url)

    def send_error(self, message, title=str, user=str, avatar_url=str, html_url=str):
        self._send_to_discord(message, 0xff0000, title, user, avatar_url, html_url)

    def send_warning(self, message, title=str, user=str, avatar_url=str, html_url=str):
        self._send_to_discord(message, 0xffff00, title, user, avatar_url, html_url)

    def send_info(self, message, title=str, user=str, avatar_url=str, html_url=str):
        self._send_to_discord(message, 0x0000ff, title, user, avatar_url, html_url)

    def _send_to_discord(self, message, color, title=str, user=str, avatar_url=str, html_url=str):
        embed = {
            "title": title,
            "description": message,
            "color": color,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "footer": {user: html_url},
            "avatar_url": avatar_url
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
import json

discord_webhook_url = os.environ['DISCORD_WEBHOOK_URL']

# Create an instance of DiscordMessenger
discord_messenger = DiscordMessenger(discord_webhook_url)

# Parse the JSON input
try:
    issue_data = json.loads(sys.argv[1])
    issue_type = sys.argv[2]
except json.JSONDecodeError:
    issue_data = {}

# Extract issue details
title = issue_data.get('title', 'No title provided')
body = issue_data.get('body', 'No body provided')
user = issue_data.get('user', 'Unknown user')
avatar_url = issue_data.get('avatar_url', '')
html_url = issue_data.get('html_url', '')

# Use the issue details to create a custom message
custom_message = f"- {title}\nDescription {body}\nUser: {user}\n[see it here]({html_url})"

# Send a message to Discord
if issue_type == 'error':
    discord_messenger.send_error(custom_message, title, user, avatar_url, html_url)
elif issue_type == 'warning':
    discord_messenger.send_warning(custom_message, title, user, avatar_url, html_url)
elif issue_type == 'info':
    discord_messenger.send_info(custom_message, title, user, avatar_url, html_url)
else:
    discord_messenger.send_message(custom_message, title, user, avatar_url, html_url)
    
    

