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

def launch_vsc(message):

    log_activity(message, "launch_vsc")
    logger.info(f"User ID: {message.chat.id}, Action: launch_vsc")

    VSC_path = PROGRAM_PATHS['VSC']
    command = f'"{VSC_path}"'
    subprocess.run(command, shell=True)
    bot.send_message(message.chat.id, '👨🏼‍💻 VSC был запущён')