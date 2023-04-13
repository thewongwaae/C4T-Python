import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")

teddy = ["Twddy", "Taddy", "Trddy", "Tnddy?", "Tmddy?"]

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	for item in teddy:
		if item in message.content:
			await message.channel.send("Did you mean Teddy?")

client.run(str(os.getenv("TOKEN")))