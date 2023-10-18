import argparse
from message_discord.message_discord import DiscordMessenger
from weather.weather import main


def function1():
    # Implement your logic for function 1 here

def function2():
    # Implement your logic for function 2 here

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run specific functions')
    parser.add_argument('function_name', choices=['function1', 'function2'], help='Name of the function to run')

    args = parser.parse_args()

    if args.function_name == 'function1':
        function1()
    elif args.function_name == 'function2':
        function2()
