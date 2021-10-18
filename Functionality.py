import random
import os
import discord
from discord import file

me = 857783875661070346

myMessageCounter = 0

"""
The following space here above the Command Center is designed for specific interactions with certain users.
I have removed all of my personal interactions with S Bot, so if you manage to download this code,
this space will be where you make functions for custom responses that only target specific users.
"""

"""The central hub for S Bot.
This takes in an author and a message, and then will call other methods in to handle his reactions to certain trigger words, message quantities, or requests.
The main code page will still handle sending the Discord messages, this page is simply handling nearly all the implementation behind the scenes
atr = The author of the current message
msg = The message that is being read to see if it has any trigger words or requests"""
def commandCenter(atr,msg):
    global myMessageCounter
    author = atr
    message = msg
    """
    Your code here, using functions made above.
    You WILL need if statements to get this to work. Make sure to have a list of User IDs you want to specifically target in order for things to work how you want them to.
    """
    return None
