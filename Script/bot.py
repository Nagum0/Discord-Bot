#Discord bot link -> https://discord.com/api/oauth2/authorize?client_id=1107026450118353049&permissions=1634235578432&scope=bot
#Username -> AstolfoBot
#Hashtag -> #2111
import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        if response.startswith("image:"):
            image_path = response[6:]

            with open(image_path, 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file=picture)
        else:
            await message.author.send(response) if is_private else await message.channel.send(response)
            
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTEwNzAyNjQ1MDExODM1MzA0OQ.Gn88Ef.rgFGbBr3eIxtvS5QgaZhk_dLjSo5rBcrSr4pgQ'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)