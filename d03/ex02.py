import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")

client.run('MTA5NjA0NTIzMDg0OTAwNzY1Nw.G4Xr71.7KaSEMcqZZ5yWGgrdoZt6MzMcoi-K7TNREdb0w')