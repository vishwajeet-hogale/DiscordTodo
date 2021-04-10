import discord 

client = discord.Client()
@client.event
async def on_ready():
  
    general_channel = client.get_channel(830510316659408936)
    await general_channel.send("Online right now !!")

client.run("ODMwNTAyMTY4NDU2NzI0NTAw.YHHnag.OnS0C0uEeJomAfLi2y5QVdO1GMs")