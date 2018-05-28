
#Floatzel bot
#copyright 2017-2018 EzioisAwesome56
import asyncio
import discord
from help import *
import random
from games import *
import time
import math
import ctypes
import re
import os
# stuff for tweetbot
import twitter
import threading
from time import sleep
from config import *
from commands import *
from discord.utils import get

print("Floatzel: Discord bot, Loading...")

# stuff for threading and twitter
lock = threading.Lock()

# threading thingy
tarray = []
client = discord.Client()

perme = "Error: you do not have permission to use this command"

# thing required for loops
loop = asyncio.get_event_loop()

# var to remember if we are broadcasting
cast = 0

# tweet getter command
def gettweet(who):
	print("Twitter thread started for "+who)
	# set an empty var for storing last id
	lastid = 0
	# main tweet loop
	while True:
		# wait 25 minutes
		sleep(1500)
		#sleep(20)
		# alright, wake the fuck up and check twitter for tweets
		tweet = api.GetUserTimeline(screen_name=who, count=1)
		# convert what we found to a list
		tlist = [i.AsDict() for i in tweet]
		# parse the tweets
		for i in tlist:
			# check if we already tweeted this
			if i['id'] == lastid:
				break
			else:
				# form the tweets into a hecking discord message format
				em = discord.Embed(color=0x481CF1, title="Link to tweet", url="https://twitter.com/"+who+"/status/"+str(i['id']))
				em.set_author(name="New Tweet from "+who, icon_url=twatcon)
				em.add_field(name="Tweet Contents:", value=i['text'])
				em.set_footer(text="Twitter")
				# store the id away dude
				lastid = i['id']
				# get the channel
				dest = client.get_channel(str(tweetchan))
				# send that shit NOW
				die = asyncio.run_coroutine_threadsafe(client.send_message(dest, embed=em), loop)
				nothing = die.result()


# Gamecyle command
def GameCycle():
	# set blank var for storing rng
	gamerng = 0
	# wait 10 seconds before starting
	sleep(10)
	while True:
		#generate a number to pick the game with
		gamerng = random.randint(0, (len(glist)-1))
		# set the playing status to it
		die = asyncio.run_coroutine_threadsafe(client.change_presence(game=discord.Game(name=glist[gamerng])), loop)
		nothing = die.result()
		#wait 10 minutes
		sleep(600)

# code used for broadcasting messages
def broadcast(message, initchan):
	global cast
	# send a message saying the broadcast is starting
	asyncio.run_coroutine_threadsafe(client.send_message(initchan, "Broadcasting message to all servers..."), loop)
	# begin the broadcast
	for server in client.servers:
		# look through every server the bot is in
		for channel in server.channels:
			# look at every channel in every server
			# check if the bot can psot in a channel, and if it can, send a message
			if channel.permissions_for(server.me).send_messages:
				# if this is running, we have found a channel! send a message to it and move the fuck on
				print("broadcasting in "+server.name+" in channel #"+channel.name)
				asyncio.run_coroutine_threadsafe(client.send_message(channel, message), loop)
				# break out of the loop so we dont hecking spam
				break
	# if we get here, we are done. send a message saying so to initchan
	asyncio.run_coroutine_threadsafe(client.send_message(initchan, "Message broadcasted!"), loop)
	# set cast to 0
	cast = 0

@client.event
async def on_message(message):
	global cast
	user = str(message.author)
	if owner == int(message.author.id):
		isown = 1
	else:
		isown = 0
	if message.content.startswith(fix+'greet'):
		await client.send_message(message.channel, greet())
	if message.content.startswith('<@339614400526942218>'):
		await client.send_message(message.channel, 'My prefix is &')
	if message.content.startswith(fix+'help'):
		await client.send_message(message.author, "Floatzel version "+ver+" help")
		time.sleep(0.01)
		await client.send_message(message.author, helptext)
	if message.content.startswith(fix+"pi"):
		await client.send_typing(message.channel)
		await client.send_message(message.channel, picmd())
	if message.content.startswith(fix+"aspam"):
		await client.send_typing(message.channel)
		await client.send_message(message.channel, aspam())
	if message.content.startswith(adminfix+'kys'):
		if isown == 1:
			await client.send_message(message.channel, ':gun:')
			await client.send_message(message.channel, ':regional_indicator_b: :regional_indicator_a: :regional_indicator_n: :regional_indicator_g:')
			print("Floatzel is exiting by user command...")
			await client.logout()
		else:
			await client.send_message(message.channel, perme)
	if message.content.startswith(fix+'kys'):
		emoji = get(client.get_all_emojis(), name='gunR')
		await client.send_message(message.channel, emoji)
		await client.send_message(message.channel, "Fuck that shit you asshole, instead of killing myself ill FUCKING KILL YOU DIPSHIT FACE")
		await client.send_message(message.channel, "**click**")
		time.sleep(0.5)
		await client.send_message(message.channel, "The one fucking time I run out of mother fucking bullets to kill an asshole, fuck my life")
	if message.content.startswith(fix+"think"):
		await client.send_message(message.channel, thonk())
	if message.content.startswith(fix+"8ball"):
		await client.send_typing(message.channel)
		await client.send_message(message.channel, eightball(message.content))
	if message.content.startswith(fix+"gf"):
		await client.send_typing(message.channel)
		await client.send_message(message.channel, girlfriend(message.content, 0))
	if message.content.startswith(fix+"bf"):
		await client.send_typing(message.channel)
		await client.send_message(message.channel, girlfriend(message.content, 1))
	if message.content.startswith(fix + "eat"):
		await client.send_typing(message.channel)
		await client.send_message(message.channel, eat(message.content))
	if message.content.startswith(fix+"invite"):
		await client.send_message(message.channel, inviteshit)
	if message.content.startswith(adminfix+'servers'):
		if isown == 1:
			msg = ""
			servers = list(client.servers)
			for x in range(len(servers)):
				msg = msg + servers[x-1].name + ", "
			await client.send_message(message.channel, msg)
		else:
			await client.send_message(message.channel, perme)
	if message.content.startswith(adminfix+'broadcast'):
		if isown == 1:
			if cast == 0:
				# first off: split the message from the command
				annc = getmsg(message.content, adminfix+"broadcast")
				if annc == 1:
					await client.send_message(message.channel, "An error happened while trying to get message to broadcast")
				# alright, at this point we should have the message
				# start the cast o matic
				cast = 1
				announce = threading.Thread(target=broadcast, args=(annc, message.channel))
				announce.start()
			else:
				await client.send_message(message.channel, "please wait until the current broadcast is done")
		else:
			await client.send_message(message.channel, perme)



# start up twitter threads
print("Floatzel is now configuring Twitter threads...")
ezio = threading.Thread(target=gettweet, args=(twat,), daemon=True)
tarray.append(ezio)
sm = threading.Thread(target=gettweet, args=(twattwo,), daemon=True)
tarray.append(sm)
print("Floatzel is now starting twitter threads...")
ezio.start()
sm.start()
# start thread for changing games
print("Floatzel is now configuring game changing thread...")
gamestate = threading.Thread(target=GameCycle, daemon=True)
tarray.append(gamestate)
print("Floatzel is now starting game changer thread...")
gamestate.start()
print("Done loading, connecting to discord...")

client.run(token, shard_count=2)