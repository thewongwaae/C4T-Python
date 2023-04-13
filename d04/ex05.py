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
	msg = message.content

	if message.author == client.user:
		return

	for item in teddy:
		if item in msg:
			await message.channel.send("Did you mean Teddy?")

	if msg.startswith('$help'):
		await message.reply("""Here is a list of all my commands:```
$help\t\t - Lists down all my available commands
$hello\t\t- Says hello!
$greet\t\t- Greets the user
$echo\t\t - Echos the user
$Say\t\t  - Impersonates the user
$rock\t\t - Play rock paper scissors
$paper\t\t|
$scisors\t|```""")
	
	if msg.startswith('$hello'):
		await message.reply('Hello!', mention_author=True)
	
	if msg.startswith('$greet'):
		await message.reply(f"Hello {message.author.name}", mention_author=True)

	if msg.startswith("$echo"):
		await message.channel.send(msg[6:].format(message))

	if msg.startswith("$Say"):
		await message.channel.send(msg[5:].format(message))
		await message.delete()
	
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