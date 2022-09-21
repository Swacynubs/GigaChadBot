import discord
import os
import youtube_dl
from discord.ext import commands
from discord import FFmpegPCMAudio

vc = ""

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.command(pass_context=True)
async def join(ctx):
	channel = ctx.message.author.voice.voice_channel
	await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
	await vc.disconnect()
	# server = ctx.message.server
	# voice_client = client.voice_client_in(server)
	# if voice_client:
	# 	await voice_client.disconnect()




	user = ctx.message.author
	print(user)
	voice_channel = user.voice.channel
	print("\nVC CHANNEL:",voice_channel)
	await voice_channel.disconnect()

@client.command(pass_context=True)
async def play(ctx):
	global vc
	user = ctx.message.author
	voice_channel = user.voice.channel
	print("Got the vc")
	channel = None
	if voice_channel != None:
		#channel = voice_channel.name
		print("GOT NAME")
		vc = await voice_channel.connect()
		vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\\bin\\ffmpeg.exe", source="01.mp3"))
		
	else:
		await client.say("DUMB NOT IN VC")

@client.command(pass_context=True)
async def chad(ctx):
	user = ctx.message.author
	voice_channel = user.voice.channel
	print("Got the vc")
	channel = None
	if voice_channel != None:
		#channel = voice_channel.name
		print("GOT NAME")
		vc = await voice_channel.connect()

		vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\\bin\\ffmpeg.exe", source="gigChad.mp3"))
		await ctx.send("GIGACHAD")
		await ctx.send(file=discord.File('gigachad-chad.gif'))
	else:
		await client.say("DUMB NOT IN VC")
# @client.event
# async def on_message(message):
# 	if message.author == client.user:
# 		return

# 	if message.content.startswith('$hello'):
# 		await message.channel.send("Hello!")

client.run('')