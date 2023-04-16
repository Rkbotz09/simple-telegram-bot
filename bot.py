from pyrogram import Client, filters
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

app.run(host='0.0.0.0', port=8080)

# Replace the values with your own API ID, API HASH and BOT TOKEN
app_id = YOUR_APP_ID
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

# Create a new Pyrogram client instance
client = Client("my_bot", app_id, api_hash, bot_token=bot_token)


# Start the client
client.start()

# Define a handler function for /start command
@client.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Hello, welcome to my bot!")


# Run the client until it's stopped
client.run()
