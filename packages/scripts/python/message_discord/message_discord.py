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

