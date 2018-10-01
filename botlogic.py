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

    charStrength = rollStats()
    charDex = rollStats()
    charCon = rollStats()
    charInt = rollStats()
    charWis = rollStats()
    charChar = rollStats()


    charRace = random.choice(raceList)
    charClass = random.choice(classList)

#############################################################
# From here until the next block is code for race modifiers.#
#############################################################
    if charRace == 'Aarakocra':
        charDex += 2
        charWis += 1
    if charRace == 'Aasimar':
        charChar += 2
    if charRace == 'Bugbear':
        charStrength += 2
        charDex += 1
    if charRace == 'Centaur':
        charStrength += 2
        charWis += 1
    if charRace == 'Changeling':
        charChar += 2

        choice = random.randint(1,2)

        if choice == 1:
            charDex += 1
        else:
            charInt += 1
    if charRace == 'Dragonborn':
        charStrength += 2
        charChar += 1
    if charRace == 'Dwarf':
        charCon += 2
    if charRace == 'Elf':
        charDex += 2
    if charRace == 'Feral Tiefling':
        charDex += 2
        charInt += 1
    if charRace == 'Firbolg':
        charWis += 2
        charStrength += 1
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
        charStrength += 2
        charCon += 1
    if charRace == 'Half-Elf':
        charChar += 2

        for x in range(2):  #There are two points to assign, so the loop iterates twice
            choice = random.randint(1,5) #Randomly assigns an ability to increment
            if choice == 1:
                charStrength += 1
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
        charStrength += 2
        charCon += 1
    if charRace == 'Hobgoblin':
        charCon += 2
        charInt += 1
    if charRace == 'Human':
        charStrength += 1
        charDex += 1
        charCon += 1
        charInt += 1
        charWis += 1
        charChar += 1
    if charRace == 'Kalashtar':
        charChar +=1
        charWis +=1

        choice = random.randint(1, 6)  # Randomly assigns an ability to increment
        if choice == 1:
            charStrength += 1
        if choice == 2:
            charDex += 1
        if choice == 3:
            charCon += 1
        if choice == 4:
            charInt += 1
        if choice == 5:
            charDex += 1
        if choice == 6:
            charChar += 1

    if charRace == 'Kenku':
        charDex += 2
        charWis += 1
    if charRace == 'Kobold':
        charDex += 2
        charStrength -= 2
    if charRace == 'Lizardfolk':
        charCon += 2
        charWis += 1
    if charRace == 'Loxodon':
        charCon += 2
        charWis += 1
    if charRace == 'Minotaur':
        charStrength += 2
        charCon += 1
    if charRace == 'Orc':
        charStrength += 2
        charCon += 1
        charInt -= 2
    if charRace == 'Shifter':
        charDex += 1
    if charRace == 'Simic Hybrid':
        charCon += 2

        choice = random.randint(1, 5)  # Randomly assigns an ability to increment
        if choice == 1:
            charStrength += 1
        if choice == 2:
            charDex += 1
        if choice == 3:
            charChar += 1
        if choice == 4:
            charInt += 1
        if choice == 5:
            charDex += 1
    if charRace == 'Tabaxi':
        charDex += 2
        charChar += 1
    if charRace == 'Tiefling':
        charChar += 2
        charInt += 1
    if charRace == 'Tortle':
        charStrength += 2
        charWis += 1
    if charRace == 'Triton':
        charStrength += 1
        charCon += 1
        charChar += 1
    if charRace == 'Vedalken':
        charInt += 2
        charWis += 1
    if charRace == 'Viashino':
        charDex += 2
        charStrength += 1
    if charRace == 'Warforged':
        charCon += 1
    if charRace == 'Yuan=ti Pureblood':
        charChar += 2
        charInt += 1

###########################
# Race modifiers end here.#
###########################

    rtn = 'Race: '+str(charRace)+'\n' +\
          'Class: '+str(charClass)+'\n\n' +\
          'Strength: '+str(charStrength)+'\n' +\
          'Dexterity: '+str(charDex)+'\n' +\
          'Constitution: '+str(charCon)+'\n' +\
          'Intelligence: '+str(charInt)+'\n' +\
          'Wisdom: '+str(charWis)+'\n' +\
          'Charisma: '+str(charChar)+'\n'

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






