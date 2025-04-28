from telethon import TelegramClient, events

api_id = 10705683
api_hash = '7844949a3031003987ea51e99177ad70'

client = TelegramClient('listener_session', api_id, api_hash)

@client.on(events.NewMessage())
async def handler(event):
    if event.is_channel:
        sender = await event.get_sender()
        print(f"📢 Channel Name: {sender.title}")
        print(f"🆔 Channel ID: {event.chat_id}")

client.start()
print("✅ Listener Bot is running... Waiting for messages.")
client.run_until_disconnected()
