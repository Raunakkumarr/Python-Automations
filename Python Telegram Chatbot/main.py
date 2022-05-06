import os
import telebot

API_KEY = os.getenv('your_bot_token')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello! Welcome to Webmatrices Telegram Bot...")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "Here are the list of commands you can use to operate this bot:\n 1. /start: to start the bot\n 2. /help: to get the command list of this bot\n 3. /greet: to get greetings from this bot\n 4. /blogs: to get updates on our blogs")

@bot.message_handler(commands=['greet'])
def send_greetings(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['blogs'])
def send_blogs(message):
	bot.reply_to(message, "Please check out our blogs at: https://blog.webmatrices.com/\nIf you want blogs on specific topic, you can send the following commands to get blogs on those topics.\n1. /blogs:coding : To get updates on Coding\n2. /blogs:python : To get updates on Python\n3. /blogs:linux : To get updates on Linux\n4. /blogs:google-adsense : To get updates on Google Adsense\n5. /blogs:business : To get updates on Business\n6. /blogs:science : To get updates on Science")

@bot.message_handler(commands=['blogs:coding'])
def send_coding_blogs(message):
	bot.reply_to(message, "Check out our Coding Blogs Here: https://blog.webmatrices.com/category/coding/")

@bot.message_handler(commands=['blogs:python'])
def send_python_blogs(message):
	bot.reply_to(message, "Check out our Blogs on Python here: https://blog.webmatrices.com/category/python/")

@bot.message_handler(commands=['blogs:linux'])
def send_linux_blogs(message):
	bot.reply_to(message, "Check out our Blogs on Linux here: https://blog.webmatrices.com/category/linux/")

@bot.message_handler(commands=['blogs:google-adsense'])
def send_adsense_blogs(message):
	bot.reply_to(message, "Check out our Blogs on Google Adsense here: https://blog.webmatrices.com/category/google-adsense/")

@bot.message_handler(commands=['blogs:business'])
def send_business_blogs(message):
	bot.reply_to(message, "Check out our Blogs on Business here: https://blog.webmatrices.com/category/business/")

@bot.message_handler(commands=['blogs:science'])
def send_science_blogs(message):
	bot.reply_to(message, "Check out our Blogs Science here: https://blog.webmatrices.com/category/science/")

bot.infinity_polling()
