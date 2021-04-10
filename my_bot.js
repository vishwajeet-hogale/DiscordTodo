const Discord = require('discord.js')
const client = new Discord.Client()

client.on('ready',()=>{
    console.log("Connected as " + client.user.tag)
    client.user.setActivity("Youtube", {type:"WATCHING"});
    client.guilds.forEach(async (guild)=>{
        await console.log(guild.name)
    });
});

client.login("ODMwNTAyMTY4NDU2NzI0NTAw.YHHnag.OnS0C0uEeJomAfLi2y5QVdO1GMs")