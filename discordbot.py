import discord
import time
import random
import os
from discord_slash import SlashCommand, SlashContext

bot = discord.Client(intents=discord.Intents.all())
token = os.environ['DISCORD_BOT_TOKEN']
# または:
# bot = commands.Bot(command_prefix='@', intents=discord.Intents.all())
slash_client = SlashCommand(bot)
guild_id = [515139485206446090]

@slash_client.slash(name="kanchome", guild_ids=guild_id)
async def _play_kanchome(message: SlashContext):
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


@bot.event
async def on_ready():
    print('kanchome ready.')

bot.run('DISCORD_BOT_TOKEN')
