import tempfile
import subprocess
import json
import telebot
from .errorLogger import is_logger_active, logger
from datetime import datetime
from colorama import Fore, Style, init

init()

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
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

BotInfo = f"""
    ╔═══════════════════════════════════════════════════╗
    ║ Запущен бот {Fore.BLUE}{bot.get_me().username}{Style.RESET_ALL}                              ║
    ║ bot. Версия {Fore.MAGENTA}{botVersion}{Style.RESET_ALL} by {Fore.MAGENTA}{dataUpdate}{Style.RESET_ALL}                  ║
    ║ lib. Версия {Fore.GREEN}telebot: {get_telebot_version()}{Style.RESET_ALL}                       ║
    ║ Дата и время запуска: {Fore.CYAN}{current_datetime}{Style.RESET_ALL}  ║
    ║ Erorr loger активен: {Fore.GREEN if logger_active else Fore.RED}{'True' if logger_active else 'False'}{Style.RESET_ALL}                         ║
    ║ {Fore.LIGHTBLACK_EX}created by ds - @qqdelet | tg - @linzaoxi{Style.RESET_ALL}         ║
    ╚═══════════════════════════════════════════════════╝)
"""


print(BotInfo)