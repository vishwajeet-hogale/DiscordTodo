rimport discord 
import pymongo
# import datatime.datetime as dt
from datetime import date
from discord.ext import commands
mongo = pymongo.MongoClient("Mongo_Server")

db = mongo["Todo-List"]

client = commands.Bot(command_prefix = "--")

@client.event
async def on_ready():
    general_channel = client.get_channel(830510316659408936)
    myEmbed = discord.Embed(title="Hello everyone ",description= "I am active",color=0x00ff00)
    myEmbed.add_field(name="Description",value="I help you make your todo list!",inline=False )
    myEmbed.add_field(name= "Date Released ",value="11th April, 2021",inline=False)
    myEmbed.set_footer(text="Please use --guide to know about me")
    myEmbed.set_author(name="Vishwajeet Hogale")
    await general_channel.send(embed=myEmbed)
@client.command(name="add",pass_context=True)
async def add(context,*,message):
    inputData = {}
    inputData["Date"] = date.today().strftime('%Y-%m-%d')
    inputData["Name"] = context.message.author.name
    inputData["Task"] = message
    todo = pymongo.collection.Collection(db,"Todo")
    todo.insert_one(inputData)
    my_embed = discord.Embed(title="Your Task has been added",description=str(context.message.content),color=0xff0000)
    await context.message.channel.send(embed=my_embed)
@client.command(name="view",pass_context=True)
async def view(context):
    query = {"Name":context.message.author.name,"Date":date.today().strftime('%Y-%m-%d')}
    todo = pymongo.collection.Collection(db,"Todo")
    if not(list(todo.find(query)) == []):
        myEmbed = discord.Embed(title="Your Tasks",description= f"Date : {date.today().strftime('%Y-%m-%d')}",color=0x0000ff)
        j = 1
    
        for i in list(todo.find(query)):
            myEmbed.add_field(name= f"Task {j}",value= i["Task"],inline=False )
            j += 1
        myEmbed.set_author(name=f"{context.message.author.name} Todo's")
        await context.message.channel.send(embed=myEmbed)
    else:
        myEmbed = discord.Embed(title="Your Tasks",description= f"Date : {date.today().strftime('%Y-%m-%d')}",color=0x0000ff)
        myEmbed.add_field(name="Tasks ",value="You have no tasks scheduled for today.",inline=False)
        await context.message.channel.send(embed=myEmbed)
    # inputData["Time_in"] = dt.now().replace("-","/")
client.run("TOKEN")
