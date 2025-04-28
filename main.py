from telethon import TelegramClient, events
import threading
from flask import Flask
import asyncio

# Your API credentials
api_id = 10705683
api_hash = '7844949a3031003987ea51e99177ad70'

# Session name (same as your uploaded session file)
session_name = 'listener_session'

# Create Telegram client
client = TelegramClient(session_name, api_id, api_hash)

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Listener Bot is running!"

# Background function to run Flask
def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Telegram message handler
@client.on(events.NewMessage)
async def handler(event):
    if event.is_channel:  # Only listen to channels, not personal chats
        chat = await event.get_chat()
        print(f"📢 New message in Channel: {chat.title} --> ID: {event.chat_id}")

async def main():
    # Start the client and run until disconnected
    await client.start()
    print("✅ Listener Bot is running... Waiting for messages...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    # Start Flask in a background thread
    threading.Thread(target=run_flask).start()

    # Start Telethon listener in main thread
    asyncio.run(main())
