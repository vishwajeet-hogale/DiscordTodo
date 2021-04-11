import discord 

client = discord.Client()
@client.event
async def on_ready():
  
    general_channel = client.get_channel(830510316659408936)
    await general_channel.send("Online right now !!")
@client.event 
async def on_message(message):
    if message.content == 'What is the version':
        general_channel = client.get_channel(830510316659408936)
        
        myEmbed = discord.Embed(title="Current Version ",description= "The bot is in Version 1.0",color=0x00ff00)
        myEmbed.add_field(name="Version code ",value="v1.0.0",inline=False )
        myEmbed.add_field(name= "Date Released ",value="11th April, 2021",inline=False)
        myEmbed.set_footer(text="This is a bot that helps you makes your todo lists! ")
        myEmbed.set_author(name="Vishwajeet Hogale")
        await general_channel.send(embed=myEmbed)
 
client.run("ODMwNTAyMTY4NDU2NzI0NTAw.YHHnag.OnS0C0uEeJomAfLi2y5QVdO1GMs")