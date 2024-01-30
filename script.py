from telethon import TelegramClient, events
import asyncio

api_id = 5013357
api_hash = '0d32f35094f14445afdd45539aa40445'

client = TelegramClient('session_name', api_id, api_hash)
sending_messages = False

bmw = ["Isetta", "sedans", "coupés", "E9", "E3", "M1", "E28", "E30", "E32", "E34", "Z1", "E31", "E36", "E38", "Z3", "E39", "E46", "X5", "Z8", "E65", "E66", "Z4", "X3", "E81", "E82", "E87", "E88", "E90", "E91", "E92", "E93", "E70", "X6", "E71", "F01", "F02", "E89", "X1", "E84", "F07", "F10", "F11", "F06", "F12", "F13", "X3F25", "F20", "F21", "F30", "F31", "F34", "i3", "F32", "F33", "F36", "F22", "F23", "F15", "F45", "F46", "i8", "X4", "F26", "F16", "F48", "G11", "G12", "G30", "G31", "F52", "G32", "G01", "F39", "G02", "G05", "G14", "G15", "G16", "G29", "G20", "G21", "F40", "G06", "X7", "G07", "F44", "G22", "G23", "G26", "iX3", "iX", "i4", "G42", "U06", "G70", "i7", "iX1", "XM", "G60", "i5", "X2", "U10", "iX2", "303", "320", "321", "326", "327", "328", "335", "340", "501", "503", "507", "700", "3200", "3/15", "3/20"]
mers = []

@client.on(events.NewMessage(outgoing=True, pattern='.bmw'))
async def bmw(event):
    chat = await event.get_chat()
    global sending_messages
    sending_messages = True

    for i in bmw:
        if sending_messages:
            await client.send_message(chat, i)
            asyncio.sleep(0.05)
        else:
            break
    sending_messages = False


@client.on(events.NewMessage(outgoing=True, pattern='.mers'))
async def mers(event):
    chat = await event.get_chat()
    global sending_messages
    sending_messages = True
    for i in mers:
        if sending_messages:
            await client.send_message(chat, i)
            asyncio.sleep(0.05)
        else:
            break
    sending_messages = False
        


@client.on(events.NewMessage(outgoing=True, pattern='.n'))
async def number(event):
    chat = await event.get_chat()
    global sending_messages
    sending_messages = True
    messageText =event.message.message

    try:
        numberText = int(messageText[3:])
    except:
        numberText = 1000

    for i in range(1, (numberText + 1)):
        if sending_messages: 
            await client.send_message(chat, f"{i}")
            await asyncio.sleep(0.05)
        else: 
            break
    sending_messages = False

@client.on(events.NewMessage(outgoing=True, pattern='.stop'))
async def stop(event):
    global sending_messages
    sending_messages = False


client.start()
client.run_until_disconnected()