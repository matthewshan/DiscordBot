import datetime
import decimal
import random
#
# This function returns how much time remains in the Fall 2018 semester.
# In terms of format, this should be applicable to any start/end date.
#
def percentFall2018():

    start = datetime.datetime(2018, 8, 27, 0, 0, 0, 0) #Start of Fall 2018, being 8/27/2018
    now = datetime.datetime.now() #Now
    end = datetime.datetime(2018, 12, 8, 0, 0 , 0 , 0) #End of Fall 2018, being 12/8/2018

    total = end-start
    daysSpent = now-start

    percentDone = (daysSpent/total) * 100
    decimalDone = decimal.Decimal(percentDone) #Converting from float to decimal

    return str(round(decimalDone, 4)) #Converting from decimal to string
#
# This function rolls 4d6, and picks the highest 3.
#
def rollStats():
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)
    d = random.randint(1,6)

    dice = [a, b, c, d]

    sorted_dice = sorted(dice, reverse=True)

    d1 = sorted_dice[0]
    d2 = sorted_dice[1]
    d3 = sorted_dice[2]

    return d1+d2+d3
#
# This function contains a list of D&D 5th Edition Races and Classes
# More importantly, it will "roll" a character with race, class, and appropriate statistic scores.
#
def rollCharacter():
    raceList = ['Aarakocra', 'Aasimar', 'Bugbear', 'Centaur', 'Changeling',
                'Dragonborn', 'Dwarf', 'Elf', 'Feral Tiefling', 'Firbolg', 'Genasi',
                'Gith', 'Gnome', 'Goblin', 'Goliath', 'Half-Elf', 'Halfling', 'Half-Orc',
                'Hobgoblin', 'Human', 'Kalashtar', 'Kenku', 'Kobold', 'Lizardfolk', 'Loxodon',
                'Minotaur', 'Orc', 'Shifter', 'Simic Hybrid', 'Tabaxi', 'Tiefling', 'Tortle',
                'Triton', 'Vedalken', 'Viashino', 'Warforged', 'Yuan-ti Pureblood']

    classList = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin',
                 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard', 'Blood Hunter']

    charStr = rollStats()
    charDex = rollStats()
    charCon = rollStats()
    charInt = rollStats()
    charWis = rollStats()
    charCha = rollStats()


    charRace = random.choice(raceList)
    charClass = random.choice(classList)

#############################################################
# From here until the next block is code for race modifiers.#
#############################################################

    races = {
		'Aarakocra':{'str': 0,'dex': 2,'con': 0, 'int': 0, 'wis': 1, 'cha': 0},
        'Aasimar':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 2},
        'Bugbear':{'str': 2, 'dex': 1, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Centaur':{'str': 2, 'dex': 0, 'con': 0, 'wis': 1, 'cha': 0},
        'Changeling':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 2},
        'Dragonborn':{'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 1},
        'Dwarf':{'str': 0, 'dex': 0, 'con': 2, 'wis': 0, 'cha': 0},
        'Elf':{'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Feral Tiefling':{'str': 0, 'dex': 2, 'con': 0, 'int': 1, 'wis': 0, 'cha': 0},
        'Firbolg':{'str': 1, 'dex': 0, 'con': 0, 'int': 0, 'wis': 2, 'cha': 0},
        'Gith':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Gnome':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Goblin':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Goliath':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Half-Elf':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Halfling':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Human':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Kalashtar':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Kenku':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Kobold':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Lizardfolk':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Loxodon':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Minotaur':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Orc':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Shifter':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Simic Hybrid':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Tabaxi':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Tiefling':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Tortle':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Triton':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Vedalken':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Viashino':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Warforged':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0},
        'Yuan-ti Pureblood':{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0}
	}
    for race in races:
        charStr += race['str']
        charDex += race['dex']
        charCon += race['con']
        charWis += race['wis']
        charCha += race['cha']

    if charRace == 'Changeling':
        choice = random.randint(1,2)
        if choice == 1:
            charDex += 1
        else:
            charInt += 1
    if charRace == 'Dragonborn':
        charStr += 2
        charCha += 1
    if charRace == 'Dwarf':
        charCon += 2
    if charRace == 'Elf':
        charDex += 2
    if charRace == 'Feral Tiefling':
        charDex += 2
        charInt += 1
    if charRace == 'Firbolg':
        charWis += 2
        charStr += 1
    if charRace == 'Genasi':
        charCon += 2
    if charRace == 'Gith':
        charInt += 1
    if charRace == 'Gnome':
        charInt += 2
    if charRace == 'Goblin':
        charDex += 2
        charCon += 1
    if charRace == 'Goliath':
        charStr += 2
        charCon += 1
    if charRace == 'Half-Elf':
        charCha += 2

        for x in range(2):  #There are two points to assign, so the loop iterates twice
            choice = random.randint(1,5) #Randomly assigns an ability to increment
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
    if charRace == 'Halfling':
        charDex += 2
    if charRace == 'Half-Orc':
        charStr += 2
        charCon += 1
    if charRace == 'Hobgoblin':
        charCon += 2
        charInt += 1
    if charRace == 'Human':
        charStr += 1
        charDex += 1
        charCon += 1
        charInt += 1
        charWis += 1
        charCha += 1
    if charRace == 'Kalashtar':
        charCha +=1
        charWis +=1

        choice = random.randint(1, 6)  # Randomly assigns an ability to increment
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

    if charRace == 'Kenku':
        charDex += 2
        charWis += 1
    if charRace == 'Kobold':
        charDex += 2
        charStr -= 2
    if charRace == 'Lizardfolk':
        charCon += 2
        charWis += 1
    if charRace == 'Loxodon':
        charCon += 2
        charWis += 1
    if charRace == 'Minotaur':
        charStr += 2
        charCon += 1
    if charRace == 'Orc':
        charStr += 2
        charCon += 1
        charInt -= 2
    if charRace == 'Shifter':
        charDex += 1
    if charRace == 'Simic Hybrid':
        charCon += 2

        choice = random.randint(1, 5)  # Randomly assigns an ability to increment
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
    if charRace == 'Tabaxi':
        charDex += 2
        charCha += 1
    if charRace == 'Tiefling':
        charCha += 2
        charInt += 1
    if charRace == 'Tortle':
        charStr += 2
        charWis += 1
    if charRace == 'Triton':
        charStr += 1
        charCon += 1
        charCha += 1
    if charRace == 'Vedalken':
        charInt += 2
        charWis += 1
    if charRace == 'Viashino':
        charDex += 2
        charStr += 1
    if charRace == 'Warforged':
        charCon += 1
    if charRace == 'Yuan=ti Pureblood':
        charCha += 2
        charInt += 1

###########################
# Race modifiers end here.#
###########################

	#Str, Dex, Con, Int, Wis, Cha

    rtn = 'Race: '+str(charRace)+'\n' +\
          'Class: '+str(charClass)+'\n\n' +\
          'Strength: '+str(charStr)+'\n' +\
          'Dexterity: '+str(charDex)+'\n' +\
          'Constitution: '+str(charCon)+'\n' +\
          'Intelligence: '+str(charInt)+'\n' +\
          'Wisdom: '+str(charWis)+'\n' +\
          'Charisma: '+str(charCha)+'\n'

    return rtn

def rockPaperScissors(hand):

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