import telebot
import json
import pyautogui

from .errorLogger import log_activity, logger

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    API_TOKEN = config['API_TOKEN']
    ALLOWED_USERS = config['ALLOWED_USERS']
    PROGRAM_PATHS = config['PROGRAM_PATHS']

bot = telebot.TeleBot(API_TOKEN)

def press_pause_button(message):

    log_activity(message, "start_record")
    logger.info(f"User ID: {message.chat.id}, Action: start_record")
    
    try:
        pyautogui.press('pause')
        bot.send_message(message.chat.id, '✅ Клавиша "Pause" нажата!')

    except Exception as e:
        bot.send_message(message.chat.id, f'❌ Произошла ошибка: {str(e)}')