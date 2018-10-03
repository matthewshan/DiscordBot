import discord
import urllib.parse
import youtube_dl
import urllib.request
import bs4
import datetime
import decimal
import random

class Bot(discord.Client):
    players = {}
    #
    # This function returns how much time remains in the Fall 2018 semester.
    # In terms of format, this should be applicable to any start/end date.
    #
    def percentFall2018(self):

        start = datetime.datetime(2018, 8, 27, 0, 0, 0,
                                  0)  # Start of Fall 2018, being 8/27/2018
        now = datetime.datetime.now()  # Now
        end = datetime.datetime(2018, 12, 8, 0, 0, 0,
                                0)  # End of Fall 2018, being 12/8/2018

        total = end - start
        daysSpent = now - start

        percentDone = (daysSpent / total) * 100
        decimalDone = decimal.Decimal(
            percentDone)  # Converting from float to decimal

        return str(round(decimalDone, 4))  # Converting from decimal to string

    #
    # This function rolls 4d6, and picks the highest 3.
    #
    def rollStats(self):
        dice = []
        for n in range(4):
            dice.append(random.randint(1, 6))

        sorted_dice = sorted(dice, reverse=True)

        d1 = sorted_dice[0]
        d2 = sorted_dice[1]
        d3 = sorted_dice[2]

        return d1 + d2 + d3

    #
    # This function contains a list of D&D 5th Edition Races and Classes
    # More importantly, it will "roll" a character with race, class, and appropriate statistic scores.
    #
    def rollCharacter(self):
        raceList = ['Aarakocra', 'Aasimar', 'Bugbear', 'Centaur', 'Changeling',
                    'Dragonborn', 'Dwarf', 'Elf', 'Feral Tiefling', 'Firbolg',
                    'Genasi',
                    'Gith', 'Gnome', 'Goblin', 'Goliath', 'Half-Elf',
                    'Halfling', 'Half-Orc',
                    'Hobgoblin', 'Human', 'Kalashtar', 'Kenku', 'Kobold',
                    'Lizardfolk', 'Loxodon',
                    'Minotaur', 'Orc', 'Shifter', 'Simic Hybrid', 'Tabaxi',
                    'Tiefling', 'Tortle',
                    'Triton', 'Vedalken', 'Viashino', 'Warforged',
                    'Yuan-ti Pureblood']

        classList = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
                     'Paladin',
                     'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard',
                     'Blood Hunter']

        charAlignment = str

        moralList = ['Lawful', 'Neutral', 'Chaotic']
        alignList = ['Good', 'Neutral', 'Evil']

        charMoral = random.choice(moralList)
        charAlign = random.choice(alignList)

        if charMoral == charAlign:
            charAlignment = 'True Neutral'
        else:
            charAlignment = charMoral + " " + charAlign

        charStr = self.rollStats()
        charDex = self.rollStats()
        charCon = self.rollStats()
        charInt = self.rollStats()
        charWis = self.rollStats()
        charCha = self.rollStats()

        charRace = random.choice(raceList)
        charClass = random.choice(classList)

        #############################################################
        # From here until the next block is code for race modifiers.#
        #############################################################

        races = {
            'Aarakocra': {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 1,
                          'cha': 0},
            'Aasimar': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0,
                        'cha': 2},
            'Bugbear': {'str': 2, 'dex': 1, 'con': 0, 'int': 0, 'wis': 0,
                        'cha': 0},
            'Centaur': {'str': 2, 'dex': 0, 'con': 0, 'wis': 1, 'cha': 0},
            'Changeling': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0,
                           'cha': 2},
            'Dragonborn': {'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0,
                           'cha': 1},
            'Dwarf': {'str': 0, 'dex': 0, 'con': 2, 'wis': 0, 'cha': 0},
            'Elf': {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0,
                    'cha': 0},
            'Feral Tiefling': {'str': 0, 'dex': 2, 'con': 0, 'int': 1,
                               'wis': 0, 'cha': 0},
            'Firbolg': {'str': 1, 'dex': 0, 'con': 0, 'int': 0, 'wis': 2,
                        'cha': 0},
            'Genasi': {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0,
                       'cha': 0},
            'Gith': {'str': 0, 'dex': 0, 'con': 0, 'int': 1, 'wis': 0,
                     'cha': 0},
            'Gnome': {'str': 0, 'dex': 0, 'con': 0, 'int': 2, 'wis': 0,
                      'cha': 0},
            'Goblin': {'str': 0, 'dex': 2, 'con': 1, 'int': 0, 'wis': 0,
                       'cha': 0},
            'Goliath': {'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0,
                        'cha': 0},
            'Half-Elf': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0,
                         'cha': 2},
            'Half-Orc': {'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0,
                         'cha': 0},
            'Halfling': {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0,
                         'cha': 0},
            'Hobgoblin': {'str': 0, 'dex': 0, 'con': 2, 'int': 1, 'wis': 0,
                          'cha': 0},
            'Human': {'str': 1, 'dex': 1, 'con': 1, 'int': 1, 'wis': 1,
                      'cha': 1},
            'Kalashtar': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 1,
                          'cha': 1},
            'Kenku': {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 1,
                      'cha': 0},
            'Kobold': {'str': -2, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0,
                       'cha': 0},
            'Lizardfolk': {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 1,
                           'cha': 0},
            'Loxodon': {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 1,
                        'cha': 0},
            'Minotaur': {'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0,
                         'cha': 0},
            'Orc': {'str': 2, 'dex': 0, 'con': 1, 'int': -1, 'wis': 0,
                    'cha': 0},
            'Shifter': {'str': 0, 'dex': 1, 'con': 0, 'int': 0, 'wis': 0,
                        'cha': 0},
            'Simic Hybrid': {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0,
                             'cha': 0},
            'Tabaxi': {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0,
                       'cha': 1},
            'Tiefling': {'str': 0, 'dex': 2, 'con': 0, 'int': 1, 'wis': 0,
                         'cha': 0},
            'Tortle': {'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 1,
                       'cha': 0},
            'Triton': {'str': 1, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0,
                       'cha': 1},
            'Vedalken': {'str': 0, 'dex': 0, 'con': 0, 'int': 2, 'wis': 1,
                         'cha': 0},
            'Viashino': {'str': 1, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0,
                         'cha': 0},
            'Warforged': {'str': 0, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0,
                          'cha': 0},
            'Yuan-ti Pureblood': {'str': 0, 'dex': 0, 'con': 0, 'int': 1,
                                  'wis': 0, 'cha': 2}
        }

        charStr += races[charRace]['str']
        charDex += races[charRace]['dex']
        charCon += races[charRace]['con']
        charWis += races[charRace]['wis']
        charCha += races[charRace]['cha']

        if charRace == 'Changeling':
            choice = random.randint(1, 2)
            if choice == 1:
                charDex += 1
            else:
                charInt += 1
        elif charRace == 'Half-Elf':
            for x in range(
                    2):  # There are two points to assign, so the loop iterates twice
                choice = random.randint(1,
                                        5)  # Randomly assigns an ability to increment
                if choice == 1:
                    charStr += 1
                if choice == 2:
                    charDex += 1
                if choice == 3:
                    charCon += 1
                if choice == 4:
                    charInt += 1
                if choice == 5:
                    charDex += 1
        elif charRace == 'Kalashtar':
            choice = random.randint(1,
                                    6)  # Randomly assigns an ability to increment
            if choice == 1:
                charStr += 1
            if choice == 2:
                charDex += 1
            if choice == 3:
                charCon += 1
            if choice == 4:
                charInt += 1
            if choice == 5:
                charDex += 1
            if choice == 6:
                charCha += 1
        elif charRace == 'Simic Hybrid':
            choice = random.randint(1,
                                    5)  # Randomly assigns an ability to increment
            if choice == 1:
                charStr += 1
            if choice == 2:
                charDex += 1
            if choice == 3:
                charCha += 1
            if choice == 4:
                charInt += 1
            if choice == 5:
                charDex += 1

        ###########################
        # Race modifiers end here.#
        ###########################

        # Str, Dex, Con, Int, Wis, Cha

        rtn = 'Race: ' + str(charRace) + '\n' + \
              'Class: ' + str(charClass) + '\n\n' + \
              'Strength: ' + str(charStr) + '\n' + \
              'Dexterity: ' + str(charDex) + '\n' + \
              'Constitution: ' + str(charCon) + '\n' + \
              'Intelligence: ' + str(charInt) + '\n' + \
              'Wisdom: ' + str(charWis) + '\n' + \
              'Charisma: ' + str(charCha) + '\n\n' + \
              'Alignment: ' + charAlignment

        return rtn

    def rockPaperScissors(self, hand):

        hand = str.lower(hand)
        moveList = ['rock', 'paper', 'scissors']

        botHand = random.choice(moveList)

        if botHand == 'rock':
            if hand == 'paper':
                return 'I chose rock! You won against me with '
            if hand == 'scissors':
                return 'I chose rock! You lost to me with '
            if hand == 'rock':
                return 'I chose rock! You tied with me using '

        if botHand == 'paper':
            if hand == 'paper':
                return 'I chose paper! You tied with me using '
            if hand == 'scissors':
                return 'I chose paper! You won against me with '
            if hand == 'rock':
                return 'I chose paper! You lost to me with '

        if botHand == 'scissors':
            if hand == 'paper':
                return 'I chose scissors! You lost to me with '
            if hand == 'scissors':
                return 'I chose scissors! You tied with me using '
            if hand == 'rock':
                return 'I chose scissors! You won against me with '

        if hand != 'scissors' or 'paper' or 'rock':
            return "¯\_(ツ)_/¯ I'm not familiar with the hand shape: "

    def checkDay(self):
        return datetime.datetime.today().weekday()

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author == self.user:
            return

        if message.content.startswith('!hello'):
            msg = 'Hello {0.author.mention}'.format(message)
            await self.send_message(message.channel, msg)

        if message.content.startswith('!fall2018'):
            msg = 'The Fall 2018 semester is ' + self.percentFall2018() + '% over.'
            await self.send_message(message.channel, msg)

        if message.content.startswith('!rollcharacter'):
            msg = 'Here is your DnD character! \n\n' + self.rollCharacter().format(
                message)
            await self.send_message(message.channel, msg)

        if message.content.startswith('!kingdedede'):
            await self.playAudio(message.author,
                      'https://www.youtube.com/watch?v=-KOlVl77SkQ&t=')

        if message.content.startswith('!denver'):
            await self.playAudio(message.author,
                      'https://www.youtube.com/watch?v=1vrEljMfXYo')

        if message.content.startswith('!stop'):
            await self.leave(message.author)

        if message.content.startswith('!play'):
            msg = message.content.format(message)
            arguments = msg.split(" ")
            reply = ""  # Create a blank string to add to
            for x in arguments[1:]:  # Skip the first element in the list
                reply += x + " "  # Add each "word" from the message as a separate string
            final = self.searchVideo(reply)  # Search for the given text on YouTube
            await self.send_message(message.channel,
                                final)  # Show video link in text chat
            await self.playAudio(message.author, final)  # Play the audio

        if 'this is so sad' in message.content:
            await self.playAudio(message.author, self.searchVideo("Despacito"))

        if message.content.startswith('!rps'):
            msg = message.content.format(message)
            arguments = msg.split(" ")
            hand = arguments[1]
            reply = self.rockPaperScissors(hand) + hand.format(message)

            await self.client.send_message(message.channel, reply)

    def searchVideo(self, request):
        search = urllib.parse.quote(request)
        print('Searching for: ' + search)
        url = "https://www.youtube.com/results?search_query=" + search
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = bs4.BeautifulSoup(html, "html.parser")
        soup.prettify()
        for anchor in soup.findAll('a',
                                   href=True):  # Iterate through links found
            if (anchor['href']).startswith('/watch?v') and 'list=' not in \
                    anchor['href']:  # Find "top" video and ignore playlists
                return ('https://www.youtube.com' + anchor['href'])

    async def playAudio(self, author, url):
        await self.leave(author)
        await self.join(author)
        await self.play(author, url)

    async def join(self, author):
        channel = author.voice.voice_channel
        await self.client.join_voice_channel(channel)

    async def leave(self, author):
        for x in self.voice_clients:
            if (x.server == author.server):
                return await x.disconnect()

    async def play(self, author, url):
        server = author.server
        voice_client = self.voice_client_in(server)
        player = await self.voice_client.create_ytdl_player(url)
        self.players[server.id] = player
        player.start()

    async def on_ready(self):
        print('------')
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

        if self.checkDay() == 6:
            with open('dedede.jpg', 'rb') as f:
                await self.edit_profile(avatar=f.read())
                await self.edit_profile(username='King DeDeDe')
                print('King DeDeDe has been selected')

        if self.checkDay() == 0:
            with open('donkey.jpg', 'rb') as f:
                await self.edit_profile(avatar=f.read())
                await self.edit_profile(username='Robo Kong')
                print('Donkey Kong has been selected')

        if self.checkDay() == 2:
            with open('diddy.jpg', 'rb') as f:
                await self.edit_profile(avatar=f.read())
                await self.edit_profile(username='Diddy Droid')
                print('Diddy Kong has been selected')

        if self.checkDay() == 4:
            with open('senorgw.jpg', 'rb') as f:
                await self.edit_profile(avatar=f.read())
                await self.edit_profile(username='Señor Game&Bot')
                print('Game and Watch has been selected')

        if self.checkDay() == 1:
            with open('duckhunt.jpg', 'rb') as f:
                await self.edit_profile(avatar=f.read())
                await self.edit_profile(username='Duck Bot')
                print('Duck Hunt has been selected')
        print('------')