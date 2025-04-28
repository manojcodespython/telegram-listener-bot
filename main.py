from telethon import TelegramClient, events
from flask import Flask
import threading

# Flask server to keep alive (for UptimeRobot if needed)
app = Flask(__name__)

@app.route('/')
def home():
    return "Listener Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

keep_alive()

# Telegram API details (same as main bot)
api_id = 10705683
api_hash = '7844949a3031003987ea51e99177ad70'
client = TelegramClient('listener_session', api_id, api_hash)

@client.on(events.NewMessage())
async def handler(event):
    try:
        if event.is_channel:
            print(f"📢 New message in Channel: {event.chat.title} --> ID: {event.chat_id}")
        elif event.is_group:
            print(f"👥 New message in Group: {event.chat.title} --> ID: {event.chat_id}")
        else:
            print(f"💬 Private chat message --> ID: {event.chat_id}")
    except Exception as e:
        print(f"❌ Error in listener: {e}")

client.start()
print("✅ Listener Bot is running... Waiting for messages...")
client.run_until_disconnected()
