import discord
import os
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")

choices = ["rock", "paper", "scissors"]

@client.event
async def on_message(message):
	msg = message.content

	if message.author == client.user:
		return
	if msg.startswith("$rock") or msg.startswith("$paper") or msg.startswith("$scissors"):
		response = random.choice(choices)
		await message.channel.send(f"I choose {response}!")

		msg = msg.replace("$", "")
		if (msg == response):
			await message.channel.send("It's a draw.")
		elif ((msg == "rock" and response == "paper") or (msg == "paper" and response == "scissors") or (msg == "scissors" and response == "rock")):
			await message.channel.send("I won!")
		elif ((msg == "paper" and response == "rock") or (msg == "scissors" and response == "paper") or (msg == "rock" and response == "scissors")):
			await message.channel.send("I lost...")

client.run(str(os.getenv("TOKEN")))