
import os
import sys
import json
from message_discord import DiscordMessenger


def main():
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
        
        
if __name__ == "__main__":
    main()