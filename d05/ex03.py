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
	
	emoji_dict = {
        ":sunglasses:": "😎",
        ":smiling_face_with_tear:": "🥲",
        ":thumbsup:": "👍",
        ":clap:": "👏",
        ":open_mouth:": "😮",
        ":partying_face:": "🥳",
        ":raised_hands:": "🙌",
    }
	emojis = list(emoji_dict.values())

	if message.author == client.user:
		return

	elif msg.startswith("$emoji_embed"):
		rand_emoji = random.choice(emojis)
		embed = discord.Embed(title="Embedded emoji", description=f"Sending emoji:\n{rand_emoji}\n--- Succesful ---", color=0xFF0000)
		await message.channel.send(embed=embed)

	elif msg.startswith("$emoji"):
		await message.channel.send(random.choice(emojis))

	elif msg.startswith("$gif"):
		dir = "assets/"
		files = [item for item in os.listdir(dir) if os.path.isfile(os.path.join(dir, item))]
		rand_file = random.choice(files)

		with open(os.path.join(dir, rand_file), 'rb') as f:
			gif = discord.File(f, filename=rand_file)
			embed = discord.Embed(title="Embedded GIF", description=f"Sending GIF:\n{gif}", color=0xFF0000)
			await message.channel.send(embed=embed, file=gif)

client.run(str(os.getenv("TOKEN")))