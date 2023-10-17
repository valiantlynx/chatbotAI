import requests
import datetime

class DiscordMessenger:
    def __init__(self, discord_webhook_url):
        self.discord_webhook_url = discord_webhook_url

    def send_message(self, message_data, color=0x00ff00):
        self._send_to_discord(message_data, color)

    def send_error(self, message_data):
        self._send_to_discord(message_data, 0xff0000)

    def send_warning(self, message_data):
        self._send_to_discord(message_data, 0xffff00)

    def send_info(self, message_data):
        self._send_to_discord(message_data, 0x0000ff)

    def _send_to_discord(self, message_data, color):
        embed = {
            "title": message_data['title'],
            "description": message_data['custom_message'],
            "color": color,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "footer": {message_data['user']: [message_data['html_url']]},
            "avatar_url": message_data['avatar_url'],
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
custom_message = f"Issue - **{title}**\n-Description: - {body}\nUser: **{user}**\n[Click Here]({html_url})"

message_data = {
    "title": title,
    "custom_message": custom_message,
    "user": user,
    "avatar_url": avatar_url,
    "html_url": html_url,
}

# Send a message to Discord
if issue_type == 'error':
    discord_messenger.send_error(message_data)
elif issue_type == 'warning':
    discord_messenger.send_warning(message_data)
elif issue_type == 'info':
    discord_messenger.send_info(message_data)
else:
    discord_messenger.send_message(message_data)
    
    

