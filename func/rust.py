import telebot
import json
import os

from .errorLogger import log_activity, logger

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    API_TOKEN = config['API_TOKEN']
    ALLOWED_USERS = config['ALLOWED_USERS']
    PROGRAM_PATHS = config['PROGRAM_PATHS']

bot = telebot.TeleBot(API_TOKEN)

def lauch_rust(message):

    log_activity(message, "lauch_rust")
    logger.info(f"User ID: {message.chat.id}, Action: lauch_rust")

    rust_path = PROGRAM_PATHS['RUST']
    os.system(rust_path)
    bot.send_message(message.chat.id, '🎮 вы запустили Rust...  🎮')