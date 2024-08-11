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

def sleep_computer(message):
    log_activity(message, "sleep_computer")
    logger.info(f"User ID: {message.chat.id}, Action: sleep_computer")

    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")