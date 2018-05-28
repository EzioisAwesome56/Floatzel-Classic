# Floatzel bot commands.py
# copyright ezioisawesome56 2017-2018
# contains command related functions to the floatzel bot
import random
import math
import time
# import stuff from other bot files
from eightball import *
from fuck import *


def greet():
   return "What the fuck do you want, i am just a simple mother fucking bot by ezioisawesome56, stfu"

def aspam():
    vert = 0
    spam = "A"
    while vert != 1999:
        spam = spam + "A"
        vert = vert + 1
    return spam

def thonk():
    dorp = 0
    oops = ":thinking: "
    while dorp != 50:
        oops = oops + ":thinking: "
        dorp = dorp + 1
    thonk = oops
    return thonk

# notes for making 8ball command
# numbers for ask again: 1, 3, 4, 5, 6, 7, 8, 10, 12, 13, 14, 16
# numbers for yes: 2, 9
# numbers for no: 11, 15
def eightball(text):
    # get the question
    split = text.split(" ", 1)
    try:
        split.remove("&8ball")
    except ValueError:
        return """**You didnt ask a fucking question, or the bot fucking broke. use your fucking brain or yell at the developer, and try the fuck again moron!**"""
    # get the question
    try:
        question = split.pop()
    except IndexError:
        return """**You didnt ask a fucking question, or the bot fucking broke. use your fucking brain or yell at the developer, and try the fuck again moron!**"""
    # generate a random number
    rng = random.randint(1, 16)
    if rng == 1 or rng == 3 or rng == 4 or rng == 5 or rng == 6 or rng == 7 or rng == 8 or rng == 10 or rng == 12 or rng == 13 or rng == 14 or rng == 16:
        gay = ballaskagain()
    elif rng == 2 or rng == 9:
        gay = ballyes()
    elif rng == 11 or rng == 15:
         gay = ballno()
    # start forming the actual message to send to the channel
    message = """**You asked:** """+question+"""\n"""+"""**Answer:** """+gay
    # return the message
    return message

def girlfriend(text, opt):
    if opt == 1:
        gender = "Boy"
    else:
        gender = "Girl"

    # get the name of the girl
    split = text.split(" ",1)
    if opt == 1:
        try:
            split.remove("&bf")
        except ValueError:
            return """**You didnt put in a name, you must hate everyone** :cry:  :cry: """
    else:
        try:
            split.remove("&gf")
        except ValueError:
            return """**You didnt put in a name, you must hate everyone** :cry:  :cry: """
    # pop the name from the list
    try:
        name = split.pop()
    except IndexError:
        return """No, a single space is not a name of any girl. get your shit together man"""
    # generate a number fro,  1-10
    rate = random.randint(0, 12)
    # call a function to deal with it because a
    bar = makebar(rate)
    hey = rate
    kkk = opt
    if rate == 11:
        rate = 0 - 1
    if rate == 12:
        rate = rate - 1
    # now that we have the bar, form the message
    msg = """**"""+gender+""":** """+name+"""\n"""+"""**Rating:** """+bar+"""\n**"""+str(rate)+""" out of 10!**\n"""+"""**Thoughts:** """+getgftxt(hey, kkk)
    # finally, return the message
    return msg

def picmd():
    time.sleep(1)
    pir = math.pi
    pi = str(pir)
    return "What, did you fucking fail 8th grade math you dumbshit?\nPi is clearly "+pi

# eat command
def eat(msg):
    # get what to eat
    split = msg.split(" ",1)
    try:
        split.remove("&eat")
    except ValueError:
        return "Im sorry, I can't eat fucking nothing dipshit!"
    try:
        object = split.pop()
    except IndexError:
        return "No, no matter how hard you fucking try, i am NOT eating nothing. Fuck off"
    # now that we have the object, determin the outcome of what will happen
    rate = random.randint(1, 7)
    eat = random.randint(1,4)
    start = """**You gave me:** """+object+"""\n**Did I eat it?** """
    if eat == 4:
        msg = start+"""NO!\n**Why not mannnnnn?** Because your food is fucking gay you dipshit moron fuckface!!"""
        return msg
    else:
        # start forming the message
        msg = start
        bigmsg = ratefood(rate, rate)
        # now that its done, finish the message
        msg = msg+"Yes\n"+bigmsg
        # return it
        return msg


inviteshit = """**Wanna invite my ass to your server? use this link!**\nhttps://discordapp.com/oauth2/authorize?\n**Wanna join my fucking house? Come join here and say hi or someshit**\n"""

def getmsg(gay, what):
    split = gay.split(" ",1)
    try:
        split.remove(what)
    except ValueError:
        return 1
    try:
        msg = split.pop()
    except IndexError:
        return 1
    # if all is well, return the msg
    return msg