from bot import Bot

file = open("TOKEN.txt")
token = file.readline()

bot = Bot()
bot.run(token)