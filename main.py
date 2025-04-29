from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os

api_id = 10705683
api_hash = '7844949a3031003987ea51e99177ad70'

# If session string already exists in file, load it
if os.path.exists("listener_session.session"):
    print("✅ Session file already exists. Using existing session...")
    client = TelegramClient("listener_session", api_id, api_hash)
else:
    print("🟡 Session file not found. Creating new session...")
    client = TelegramClient("listener_session", api_id, api_hash)
    client.start()  # This line will ask for your number and OTP only once
    print("✅ Session created and saved automatically!")

with client:
    print("🎯 Bot is live and connected to Telegram.")
