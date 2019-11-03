import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

@client.event
async def on_voice_state_update(member, before, after):
    print(member)

# token にDiscordのデベロッパサイトで取得したトークンを入れてください
client.run("NjQwMTc1MDcxODkzMTI3MTg5.Xb1_0g.ADpTPKuAheHoAqw_ZtvV1UZdRmo")
