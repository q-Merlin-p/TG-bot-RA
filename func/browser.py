import telebot
import webbrowser
import json
from .errorLogger import log_activity, logger
from PIL import ImageGrab 



with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    API_TOKEN = config['API_TOKEN']
    ALLOWED_USERS = config['ALLOWED_USERS']
    PROGRAM_PATHS = config['PROGRAM_PATHS']

bot = telebot.TeleBot(API_TOKEN)

def open_url(message, url):
    webbrowser.open(url)

def get_url_from_action(message, action):
    log_activity(message, "Открыть заготовленную ссылку")
    logger.info(f"User ID: {message.chat.id}, Action: Открыть заготовленную ссылку")
    return config.get('urls', {}).get(action, '')

def open_custom_url(url, chat_id):
    if chat_id in ALLOWED_USERS:
        try:
            webbrowser.open(url)
            return '🌐 Ссылка была успешно открыта в браузере.'
        except Exception as e:
            return f'❌ Ошибка при открытии ссылки: {str(e)}'
    else:
        return '❌ Извините, у вас нет разрешения использовать этого бота.'