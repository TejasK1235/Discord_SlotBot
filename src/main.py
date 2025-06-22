import random
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from slot_machine_logic import SlotMachine
from responses import get_response

# Loading token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot setup
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

slot_machine = SlotMachine()

# Message functionality
async def send_message(message: Message, user_message: str):
    if not user_message:
        print("Message is empty!")
        return
    
    is_private = user_message[0] == "?"
    user_message = user_message[1:] if is_private else user_message

    try:
        parts = user_message.split()
        command = parts[0]

        if command == "!slot":
            if len(parts) == 3:
                bet = parts[1]
                lines = parts[2]
                response = await slot_machine.play(message.author, bet, lines)
            else:
                response = "Usage: !slot <bet> <lines>"
        elif command == "!setbalance":
            if len(parts) == 2:
                amount = parts[1]
                response = slot_machine.set_balance(message.author, amount)
            else:
                response = "Usage: !setbalance <amount>"
        elif command == "!deposit":
            if len(parts) == 2:
                amount = parts[1]
                response = slot_machine.deposit(message.author, amount)
            else:
                response = "Usage: !deposit <amount>"
        elif command=="!commands":
            response="Set initial balance: !setbalance <amount>\nDeposit additional amount: !deposit <amount>\nStart playing: !slot <bet> <lines>"
        else:
            response = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

        bot_username = str(client.user)
        bot_channel = str(message.channel)
        print(f"[{bot_channel}] [{bot_username}]: {response}")

    except Exception as e:
        print(e)


# Starting the bot
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now online")

# Handling incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username = str(message.author)
    channel = str(message.channel)
    user_message = str(message.content)

    print(f"[{channel}] [{username}]: {user_message}")
    await send_message(message, user_message)

def main():
    client.run(TOKEN)

if __name__ == "__main__":
    main()
