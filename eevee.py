try:
    from lib import discord
    from lib.discord.ext.commands import Bot
    from lib.discord.ext import commands
    import asyncio
    import datetime
    import linecache
    import os
    import sys
    import time
    from lib import config_file_read
except Exception as e:
    print('[ ERROR ] Module Error:', e)

try:
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, '')
except Exception as e:
    print("[ ERROR ] Path Error:", e)

try:
    config = config_file_read.Cfg()
except Exception as e:
    print('[ ERROR ] Config Module Error:', e)
    time.sleep(5)
    sys.exit()
else:
    try:
        TOKEN = config.TOKEN
        LOG_CHANNEL = config.LOG_CHANNEL
        NEW_MEMBER_CHANNEL = config.NEW_MEMBER_CHANNEL
        PREFIX = config.PREFIX
    except Exception as e:
        print('[ ERROR ] Config Module Error:', e)
        time.sleep(5)
        sys.exit()


try:
    file = config_file_read.FileRead()
except Exception as e:
    print('[ ERROR ] File Module Error:', e)
else:
    try:
        wsite = file.wsite
        hellonewuser = file.hellonewuser
    except Exception as e:
            print('[ ERROR ] File Module Error:', e)



try:
    client = commands.Bot(command_prefix = PREFIX)
except Exception as e:
    print('[ ERROR ] Prefix Error:', e)
    time.sleep(5)
    sys.exit()



@client.event
async def on_ready():
    os.system('cls')
    print("[ Starting Up ]")
    time.sleep(3)
    os.system('cls')
    print("[ Connecting... ]")
    time.sleep(3)
    os.system('cls')
    print("[ Logging to the server... ]")
    time.sleep(3)
    os.system('cls')
    print('[' + ' Logged in ' + ']' + '  Name: ' + client.user.name + ' | ' + 'ID: ' + client.user.id + ' | ' + 'Prefix: ' + config.PREFIX)



# await client.process_commands(message)


@client.command()
async def ping():
    try:
        time = datetime.datetime.now()
        await client.say("Pong!")
        print('[' + ' Action ' + '] ' + time.strftime("%H:%M %d.%m.%Y") + ' | ' +  'ping' + ' command has been used.')
    except Exception as e:
        print("[ ERROR ] Ping Command Error:", e)

@client.command()
async def rules():
    try:
        await client.say("Rules off the server.")
        time = datetime.datetime.now()
        print('['  + ' Action ' + '] ' + time.strftime("%H:%M %d.%m.%Y") + ' | ' +  'rules' + ' command has been used.')
    except Exception as e:
        print("[ ERROR ] Rules Command Error:", e)

@client.command()
async def website():
    try:
        await client.say(wsite)
        time = datetime.datetime.now()
        print('['  + ' Action ' + '] ' + time.strftime("%H:%M %d.%m.%Y") + ' | ' +   'website' + ' command has been used.')
    except Exception as e:
        print("[ ERROR ] Website Command Error:", e)

@client.command()
async def echo(*args):
    try:
        output = ''
        for word in args:
            output += word
            output += ' '
        await client.say(output)
        time = datetime.datetime.now()
        print('[' +  ' Action ' +  '] ' + time.strftime("%H:%M %d.%m.%Y") + ' | ' +   'echo' +  ' command has been used.')
    except Exception as e:
        print("[ ERROR ] Echo Command Error:", e)

# Kick command - syntax: <prefix>kick <username>
@client.command(pass_context = True)
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.User):
    await client.kick(member)
    time = datetime.datetime.now()
    em = discord.Embed(title=str(member), description=time.strftime("Date: %d.%m.%Y Time: %H:%M"), colour=0xFF0000)
    em.set_author(name='Member Kicked', icon_url=client.user.default_avatar_url)
    await client.send_message(discord.Object(id=LOG_CHANNEL), embed=em)
    await client.say("__**Successfully User Has Been Kicked!**__")
    print('[' +  ' Action ' +  '] ' + time.strftime("%H:%M %d.%m.%Y") + ' | '  + str(member)  + ' has been kicked!')

# Ban command - syntax: <prefix>ban <username>
@client.command(pass_context = True)
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.User):
    await client.ban(member)
    time = datetime.datetime.now()
    em = discord.Embed(title=str(member), description=time.strftime("Date: %d.%m.%Y Time: %H:%M"), colour=0xFF0000)
    em.set_author(name='Member Banned', icon_url=client.user.default_avatar_url)
    await client.send_message(discord.Object(id=LOG_CHANNEL), embed=em)
    await client.say("__**Successfully User Has Been Banned!**__")
    print('[' +  ' Action ' +  '] ' + time.strftime("%H:%M %d.%m.%Y") + ' | '  + str(member) +  ' has been banned!')

# Clear messages command - syntax: <prefix>clear <amount>
@client.command(pass_context = True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Message has been deleted.')
    time = datetime.datetime.now()
    print('[' +  ' Action ' +  '] ' + time.strftime("%H:%M %d.%m.%Y") + ' | ' +   'clear' +  ' command has been used.')

# When someone has join to server.
@client.event
async def on_member_join(member):
    time = datetime.datetime.now()
    em = discord.Embed(title=str(member), description=time.strftime("Date: %d.%m.%Y Time: %H:%M"), colour=0x33FF33)
    em.set_author(name='Member Joined', icon_url=client.user.default_avatar_url)
    await client.send_message(discord.Object(id=LOG_CHANNEL), embed=em)
    await client.send_message(discord.Object(id=NEW_MEMBER_CHANNEL), "**" + str(member) + "**" + " has join to our community! " + time.strftime("Date: %d.%m.%Y Time: %H:%M"))
    await client.send_message(member, hellonewuser)
    print('[' + ' Action ' + '] ' + time.strftime("%H:%M %d.%m.%Y") + ' | ' + str(member) +  ' has join to server!')

# When someone has left the server.
@client.event
async def on_member_remove(member):
    time = datetime.datetime.now()
    em = discord.Embed(title=str(member), description=time.strftime("Date: %d.%m.%Y Time: %H:%M"), colour=0xFF9933)
    em.set_author(name='Member Left', icon_url=client.user.default_avatar_url)
    await client.send_message(discord.Object(id=LOG_CHANNEL), embed=em)
    print('[' +  ' Action ' +  '] ' + time.strftime("%H:%M %d.%m.%Y") + ' | ' +  str(member) + ' has left the server!')

# TOKEN is in the config.ini
try:
    client.run(TOKEN)
except Exception as e:
    print('[ ERROR ] Token Error:', e)
    time.sleep(5)
    sys.exit()
