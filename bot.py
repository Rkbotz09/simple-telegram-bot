import os
from pyrogram import Client, filters
from app import app

# Replace the values with your own API ID, API HASH and BOT TOKEN
app_id = 21973813
api_hash = 'c578b64ac7af52f363f9e0ebfbc67923'
bot_token = '5837194490:AAGvf78CyVNPMDFxg78mt4vk3-LMYmwtH_Y'

# Create a new Pyrogram client instance
client = Client("my_bot", app_id, api_hash, bot_token=bot_token)


# Define a handler function for /start command
@client.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Hello, welcome to my bot!")


# Run the client until it's stopped
if __name__ == '__main__':
    client.start()
    app.run()
    client.run()

