import discord
import time
import random
import os

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "!kanchome":
        try:
            voich = await discord.VoiceChannel.connect(message.author.voice.channel)
            voice_client = message.guild.voice_client
            num = random.randint(1, 5)
            source = discord.FFmpegPCMAudio(str(num)+".mp3")
            voice_client.play(source)
            time.sleep(2)
            await voich.disconnect()
        except AttributeError:
            num = random.randint(1, 5)
            if num == 1:
                await message.channel.send("………なんのつもりだい？ " + message.author.name + "。")
            elif num == 2:
                await message.channel.send("ふわあ…" + message.author.name + "、今日はもう寝ないかい？僕もう眠いんだ…")
            elif num == 3:
                await message.channel.send("おはよう" + message.author.name + "！" + message.author.name + "は今朝もカッコイイぜ！")
            elif num == 4:
                await message.channel.send( message.author.name + "ーー！！　大事なコンサートほっぽりだして何やってんだよー！")
            elif num == 5:
                await message.channel.send("フゥ…やっとミラノに帰れるんだ…　あれ？あんなところにお菓子が落ちてるぞ。もったいないなあ…　あれ？船が動きだして…　わーーー" + message.author.name + "ーーーー!!!")
    if message.content == "!friend":
        try:
            voich = await discord.VoiceChannel.connect(message.author.voice.channel)
            voice_client = message.guild.voice_client
            source = discord.FFmpegPCMAudio(str(5)+".mp3")
            voice_client.play(source)
            time.sleep(2)
            await voich.disconnect()
        except AttributeError:
            num = random.randint(1, 10)
            if num == 1:
                await message.channel.send("フォルゴレ、いくよ!!!　僕の友達を、ここまでひどい目にあわせた" + message.author.name + "を、ケチョンケチョンにやっつけてやるんだ!!")
            else:
                await message.channel.send(message.author.name + "。ボクたち、友達だろ？")
    if message.content == "!mon":
        try:
            voich = await discord.VoiceChannel.connect(message.author.voice.channel)
            voice_client = message.guild.voice_client
            source = discord.FFmpegPCMAudio("mon.mp3")
            voice_client.play(source)
            time.sleep(19)
            await voich.disconnect()
        except AttributeError:
            await message.channel.send("GG!")
    if message.content == "!hotaru":
        try:
            voich = await discord.VoiceChannel.connect(message.author.voice.channel)
            voice_client = message.guild.voice_client
            source = discord.FFmpegPCMAudio("hotaru.mp3")
            voice_client.play(source)
            time.sleep(35)
            await voich.disconnect()
        except AttributeError:
            await message.channel.send("お疲れ!" + message.author.name + "!")
    if message.content == "!hotaru-full":
        try:
            voich = await discord.VoiceChannel.connect(message.author.voice.channel)
            voice_client = message.guild.voice_client
            source = discord.FFmpegPCMAudio("hotaru_full.mp3")
            voice_client.play(source)
            time.sleep(212)
            await voich.disconnect()
        except AttributeError:
            await message.channel.send("この曲ちょっと長くない？")
    if message.content == "!hotaru-nare":
        try:
            voich = await discord.VoiceChannel.connect(message.author.voice.channel)
            voice_client = message.guild.voice_client
            source = discord.FFmpegPCMAudio("nare.mp3")
            voice_client.play(source)
            time.sleep(35)
            await voich.disconnect()
        except AttributeError:
            await message.channel.send("ふわあ…" + message.author.name + "、今日はもう寝ないかい？僕もう眠いんだ…")



            

client.run(token)
