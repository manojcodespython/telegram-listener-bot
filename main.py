from telethon import TelegramClient, events

api_id = 10705683
api_hash = '7844949a3031003987ea51e99177ad70'

client = TelegramClient('listener_session', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    if event.is_channel:
        print(f"📣 Channel Name: {event.chat.title}")
        print(f"🆔 Channel ID: {event.chat_id}")
        print(f"💬 Message: {event.message.message}\n")

client.start()
client.run_until_disconnected()
