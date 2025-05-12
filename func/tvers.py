eeeeimport tempfile
import subprocess
import json
import telebot
from .errorLogger import is_logger_active, logger
from datetime import datetime
from colorama import Fore, Style, init

init()

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    ALLOWED_USERS = config['ALLOWED_USERS']
    API_TOKEN = config['API_TOKEN']
    botVersion = config['botVersion']
    dataUpdate = config['dataUpdate']

bot = telebot.TeleBot(API_TOKEN)
logger_active = is_logger_active(logger)
current_datetime = datetime.now()

def get_telebot_version():
    try:
        result = subprocess.check_output(['pip', 'show', 'pytelegrambotapi']).decode('utf-8')
        lines = result.strip().split('\n')
        for line in lines:
            if line.startswith('Version:'):
                return line.split(': ')[1].strip()
        return 'Не удалось определить версию'
    except subprocess.CalledProcessError:
        return 'Не удалось определить версию'

def check_user_permission(func):
    def wrapper(arg):
        chat_id = None
        
        if isinstance(arg, telebot.types.CallbackQuery):
            chat_id = arg.message.chat.id
        elif isinstance(arg, telebot.types.Message):
            chat_id = arg.chat.id

        if chat_id not in ALLOWED_USERS:
            bot.send_message(chat_id, '❌ Извините, у вас нет разрешения использовать этого бота.')
            return
        return func(arg)
    return wrapper

BotInfo = f"""
    ╔═══════════════════════════════════════════════════╗
    ║ Запущен бот {Fore.BLUE}{bot.get_me().username}{Style.RESET_ALL}                             ║
    ║ bot. Версия {Fore.MAGENTA}{botVersion}{Style.RESET_ALL} by {Fore.MAGENTA}{dataUpdate}{Style.RESET_ALL}                  ║
    ║ lib. Версия {Fore.GREEN}telebot: {get_telebot_version()}{Style.RESET_ALL}                       ║
    ║ Дата и время запуска: {Fore.CYAN}{current_datetime}{Style.RESET_ALL}  ║
    ║ Erorr loger активен: {Fore.GREEN if logger_active else Fore.RED}{'True' if logger_active else 'False'}{Style.RESET_ALL}                         ║
    ║ {Fore.LIGHTBLACK_EX}created by ds - devxzcd {Style.RESET_ALL}               ║
    ╚═══════════════════════════════════════════════════╝
"""


print(BotInfo)
