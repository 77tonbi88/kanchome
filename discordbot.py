import discord
import time
import asyncio
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
            source = discord.FFmpegPCMAudio(str(num) + ".mp3")
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
                await message.channel.send(message.author.name + "ーー！！ 大事なコンサートほっぽりだして何やってんだよー！")
            elif num == 5:
                await message.channel.send("フゥ…やっとミラノに帰れるんだ…　あれ？あんなところにお菓子が落ちてるぞ。もったいないなあ…　あれ？船が動きだして…　わーーー" + message.author.name + "ーーーー!!!")
    if message.content == "!friend":
        try:
            voich = await discord.VoiceChannel.connect(message.author.voice.channel)
            voice_client = message.guild.voice_client
            source = discord.FFmpegPCMAudio(str(5) + ".mp3")
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
    if message.content == "!fuck":
        try:
            voich = await discord.VoiceChannel.connect(message.author.voice.channel)
            voice_client = message.guild.voice_client
            source = discord.FFmpegPCMAudio("fuck_you_bitch.mp3")
            voice_client.play(source)
            time.sleep(10)
            await voich.disconnect()
        except AttributeError:
            await message.channel.send("Fuck you bitch!! Fuck you mother!!")
    if message.content == "!gururi":
        try:
            voich = await discord.VoiceChannel.connect(message.author.voice.channel)
            voice_client = message.guild.voice_client
            source = discord.FFmpegPCMAudio("gururi.mp3")
            voice_client.play(source)
            time.sleep(30)
            await voich.disconnect()
        except AttributeError:
            num = random.randint(1, 100)
            if num == 10:
                await message.channel.send(":left_facing_fist: :rage: :right_facing_fist: ")
            else:
                await message.channel.send(":last_quarter_moon_with_face: :woozy_face: :first_quarter_moon_with_face: ")
    if message.content == "!imai":
        await message.channel.send("今井…恭平")
    if message.content == "!ono":
        await message.channel.send("小野...ヒデアキ")
    if message.content == "!kodera":
        await message.channel.send("コデラ...24")
    if message.content == "!katayama1":
        try:
            voich = await discord.VoiceChannel.connect(message.author.voice.channel)
            voice_client = message.guild.voice_client
            source = discord.FFmpegPCMAudio("onnna.mp3")
            voice_client.play(source)
            time.sleep(10)
            await voich.disconnect()
        except AttributeError:
            await message.channel.send("？？「女はサンドバック」")
    if message.content == "!katayama2":
        try:
            voich = await discord.VoiceChannel.connect(message.author.voice.channel)
            voice_client = message.guild.voice_client
            source = discord.FFmpegPCMAudio("onnna2.mp3")
            voice_client.play(source)
            time.sleep(10)
            await voich.disconnect()
        except AttributeError:
            await message.channel.send("？？「女はサンドバック」")
    if message.content == "!katayama":
        num = random.randint(1, 4)
        if num == 1:
            try:
                voich = await discord.VoiceChannel.connect(message.author.voice.channel)
                voice_client = message.guild.voice_client
                source = discord.FFmpegPCMAudio("onnna.mp3")
                voice_client.play(source)
                time.sleep(10)
                await voich.disconnect()
            except AttributeError:
                await message.channel.send("？？「女はサンドバック」")
        elif num == 2:
            await message.channel.send("？？「うちがあいてになったる！」")
        elif num == 3:
            await message.channel.send("？？「女は殴るためにいる」")
        elif num == 4:
            await message.channel.send("？？「女はサンドバック」")
    if message.content == "!yamanaka":
        num = random.randint(1, 2)
        if num == 1:
            await message.channel.send("？？「デブでしか抜けん」")
        elif num == 2:
            await message.channel.send("？？「中学生時代のあだ名は歩く18禁」")
    if message.content == "!delchat":
        try:
            if discord.utils.get(message.author.roles):
                msgs = []
                msgs = [msg async for msg in message.channel.history(limit=10)]
                author_info = msgs[0].author.id
                for msg in msgs:
                    await message.channel.send(msg.author.id)
                    if author_info != msg.author.id:
                        msgs.remove(msg)
                await message.channel.delete_messages(msgs)
                await message.channel.send("削除が完了したよ～")
                await asyncio.sleep(4)
                await message.channel.purge(limit=1)
            else:
                await message.channel.send("権限がありません")
        except AttributeError:
            await message.channel.send("うまくいかなかったよ～")

client.run(token)
