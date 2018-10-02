# Work with Python 3.6
import discord
import botlogic
import urllib.parse
import youtube_dl
import urllib.request
import bs4

file = open("TOKEN.txt")
TOKEN = file.readline()

client = discord.Client()

players = {}

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!fall2018'):
        msg = 'The Fall 2018 semester is '+botlogic.percentFall2018()+'% over.'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!rollcharacter'):
        msg = 'Here is your DnD character! \n\n'+botlogic.rollCharacter().format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!kingdedede'):
        await playAudio(message.author, 'https://www.youtube.com/watch?v=-KOlVl77SkQ&t=')

    if message.content.startswith('!denver'):
        await playAudio(message.author, 'https://www.youtube.com/watch?v=1vrEljMfXYo')

    if message.content.startswith('!stop'):
        await leave(message.author)

    if message.content.startswith('!play'):
        msg = message.content.format(message)
        arguments = msg.split(" ")
        reply = "" #Create a blank string to add to
        for x in arguments[1:]: #Skip the first element in the list
            reply += x+" " #Add each "word" from the message as a separate string
        final = searchVideo(reply) #Search for the given text on YouTube
        await client.send_message(message.channel, final) #Show video link in text chat
        await playAudio(message.author, final) #Play the audio

    if 'this is so sad' in message.content:
        await playAudio(message.author, searchVideo("Despacito"))

    if message.content.startswith('!rps'):
        msg = message.content.format(message)
        arguments = msg.split(" ")
        hand = arguments[1]
        reply = botlogic.rockPaperScissors(hand)+hand.format(message)

        await client.send_message(message.channel, reply)


def searchVideo(request):

    search = urllib.parse.quote(request)
    print('Searching for: '+search)
    url = "https://www.youtube.com/results?search_query="+search
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = bs4.BeautifulSoup(html, "html.parser")
    soup.prettify()
    for anchor in soup.findAll('a', href=True): #Iterate through links found
        if(anchor['href']).startswith('/watch?v') and 'list=' not in anchor['href']: #Find "top" video and ignore playlists
            return ('https://www.youtube.com'+anchor['href'])

async def playAudio(author, url):
    await leave(author)
    await join(author)
    await play(author, url)

async def join(author):
    channel = author.voice.voice_channel
    await client.join_voice_channel(channel)

async def leave(author):
    for x in client.voice_clients:
        if(x.server == author.server):
            return await x.disconnect()

async def play(author, url):
    server = author.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()


@client.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    if botlogic.checkDay() == 6:
        with open('dedede.jpg', 'rb') as f:
            await client.edit_profile(avatar=f.read())
            await client.edit_profile(username='King DeDeDe')
            print('King DeDeDe has been selected')

    if botlogic.checkDay() == 0:
        with open('donkey.jpg', 'rb') as f:
            await client.edit_profile(avatar=f.read())
            await client.edit_profile(username='Robo Kong')
            print('Donkey Kong has been selected')

    if botlogic.checkDay() == 2:
        with open('diddy.jpg', 'rb') as f:
            await client.edit_profile(avatar=f.read())
            await client.edit_profile(username='Diddy Droid')
            print('Diddy Kong has been selected')

    if botlogic.checkDay() == 4:
        with open('senorgw.jpg', 'rb') as f:
            await client.edit_profile(avatar=f.read())
            await client.edit_profile(username='Señor Game&Bot')
            print('Game and Watch has been selected')
    if botlogic.checkDay() == 1:
        with open('duckhunt.jpg', 'rb') as f:
            await client.edit_profile(avatar=f.read())
            await client.edit_profile(username='Duck Bot')
            print('Duck Hunt has been selected')
    print('------')

client.run(TOKEN)
