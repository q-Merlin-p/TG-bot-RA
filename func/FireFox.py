import telebot
import json
import subprocess
from .errorLogger import log_activity, logger

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    API_TOKEN = config['API_TOKEN']
    ALLOWED_USERS = config['ALLOWED_USERS']
    PROGRAM_PATHS = config['PROGRAM_PATHS']

bot = telebot.TeleBot(API_TOKEN)

def launch_FIREFOX(message):

    log_activity(message, "launch_FIREFOX")
    logger.info(f"User ID: {message.chat.id}, Action: launch_FIREFOX")

    FIREFOX_path = PROGRAM_PATHS['FIREFOX']
    command = f'"{FIREFOX_path}"'
    subprocess.run(command, shell=True)
    bot.send_message(message.chat.id, '🦊 FIREFOX был запущён')