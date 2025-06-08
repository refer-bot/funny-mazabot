import telebot
import random

# Tera BotFather token
TOKEN = '7818509267:AAELp1HWBi3PAcisCcrEUeBXiFPKoITKipk'
bot = telebot.TeleBot(TOKEN)

# Funny responses ka collection
jokes = [
    "Arre, tu kya programmer hai? Tab toh tera dil bhi binary mein dhadakta hoga! 😜",
    "Ek baar computer ne apne bhai se kaha: 'Bhai, tu thodi RAM badha!' 😅",
    "Pyaar wali coffee: Espresso Yourself! ☕😉",
    "Mujhe kyun lagta hai tu aaj bot se baat karke hasne wala hai? 😎",
    "Chai peete peete code likha jaaye, ya code likhte likhte chai piya jaaye? 😜"
]

# /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Arre {message.from_user.first_name}, welcome to Funny MazaBot! 😜 Bol, kya masti karein? Type /joke for a thanda joke ya /help for options!")

# /joke command
@bot.message_handler(commands=['joke'])
def send_joke(message):
    random_joke = random.choice(jokes)
    bot.reply_to(message, random_joke)

# /help command
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Main hoon Funny MazaBot! 😎 Commands hain:\n/joke - Ek mast joke suno\n/start - Masti shuru karo\nYa kuch bhi type kar, main thodi si masti kar dunga!")

# Random messages ke liye
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    responses = [
        f"Arre {message.from_user.first_name}, ye kya bola tune? 😅 Kuch aur try kar!",
        "Haha, tu bhi na, seedha joke maang le! 😜 Type /joke",
        "Oye, itna serious kyun hai? Ek smile toh banta hai! 😎",
        "Tera message padh ke lagta hai tu bhi chai lover hai! ☕ Bol, kya scene hai?"
    ]
    bot.reply_to(message, random.choice(responses))

# Bot ko start karo
try:
    bot.infinity_polling()
except Exception as e:
    print(f"Error: {e}")