import asyncio
from telethon import TelegramClient, events

api_id = 25521514  # Your API ID
api_hash = '78e89cfc0f1c8b9d25a1a7c2b6c0b07b'  # Your API HASH

session_name = 'forwarder_session'  # Your .session filename without .session extension
client = TelegramClient(session_name, api_id, api_hash)

async def main():
    @client.on(events.NewMessage)
    async def handler(event):
        try:
            sender = await event.get_sender()
            if event.chat and event.chat.title:
                print(f"🔵 Channel Name: {event.chat.title}")
                print(f"🆔 Channel ID: {event.chat_id}\n")
        except Exception as e:
            print(f"Error: {e}")

    print("✅ Listener Bot started successfully. Waiting for messages...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
