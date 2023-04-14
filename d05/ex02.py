import discord
import os
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
	msg = message.content
	emojis = [":sunglasses:", ":smiling_face_with_tear:", ":thumbsup:", ":clap:", ":open_mouth:", ":partying_face:",":raised_hands:"]

	if message.author == client.user:
		return

	if msg.startswith("$emoji"):
		await message.channel.send(random.choice(emojis))

	if msg.startswith("$emoji_embed"):
		rand_emoji = random.choice(emojis)
		embed = discord.Embed(title="Embedded emoji", description=f"Sending emoji:\n{rand_emoji}\n--- Succesful ---", color=0xFF0000)
		await message.channel.send(embed)

client.run(str(os.getenv("TOKEN")))