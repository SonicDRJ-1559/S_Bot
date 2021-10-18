import discord
import Token
import Functionality
import random

DISCORD_TOKEN = Token.getToken()

client = discord.Client()

me = 863082356918321193 #This is the User ID for S Bot. This is required for the shoot command since otherwise it won't know if it's shooting itself

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    incomingmsg = message.content
    author = message.author
    shoot = ["Shoot_1.gif", "Shoot_2.gif","Shoot_3.gif","Shoot_5.gif","Shoot_6.gif","Shoot_7.gif","Shoot_8.gif","Shoot_9.gif","Shoot_10.gif","Shoot_11.gif","Shoot_12.gif","Shoot_13.gif","Shoot_14.gif","Shoot_15.gif"]
    #Sees that the message is from this bot, and ignores it
    if message.author == client.user:
        return 0
    """The following if statement is used for the Shoot command phrase.
        What happens, is that it creates a for loop, where the maximum value for variable 'i' is how many people were pinged.
        from there, it sends individual shoot messages, depending upon who the target is, as well as who the author is.
        If the author shoots themselves, the bot clearly states that they have wished to fire upon their own position.
        If the author designates a separate target, then it says they fired upon the target's position.
        If the author tries to shoot S Bot, S Bot simply replies that he is too smart for them, and doesn't shoot himself.
        This means that the Shoot command has, in theory, no real limit to how many people it can target on one command, unless Discord
        itself has a ping limit per message."""
    if message.content.startswith("s!shoot"):
        for i in range(0,len(message.mentions)):
            member = message.mentions[i]
            if message.author == member:
                #This handles if the person doing the shooting is also the target
                await message.channel.send("{atr} has requested we fire upon their position".format(atr = message.author.mention), file=discord.File(random.choice(shoot)))
            elif member.id == me:
                #This handles if the person is trying to shoot S Bot
                await message.channel.send("Hah! You fool! I control the guns! I know my own position when I see it!")
            else:
                #This handles all generic shooting of one person to another
                await message.channel.send("{atr} has requested we fire upon {target}'s position".format(atr = message.author.mention, target = member.mention), file=discord.File(random.choice(shoot)))
    else:
        #This activates for all hard-coded commands, which are person specific.
        newMessage = Functionality.commandCenter(author, incomingmsg)
        if newMessage != None and newMessage != "" and newMessage != " ":
            await message.channel.send(newMessage)

client.run(DISCORD_TOKEN)