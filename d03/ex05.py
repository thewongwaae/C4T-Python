import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith('$hello'):
		await message.reply('Hello!', mention_author=True)
	if message.content.startswith('$greet'):
		await message.reply(f"Hello {message.author.name}", mention_author=True)

client.run(str(os.getenv("TOKEN")))