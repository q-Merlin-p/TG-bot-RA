import telebot
import tempfile
import json
from PIL  import ImageGrab 
import os
import psutil
import webbrowser
import pyautogui
import subprocess
import time
import threading

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    API_TOKEN = config['API_TOKEN']
    ALLOWED_USERS = config['ALLOWED_USERS']
    PROGRAM_PATHS = config['PROGRAM_PATHS']

bot = telebot.TeleBot(API_TOKEN)

def turn_on_discord(message):
    discord_path = PROGRAM_PATHS['Discord']
    os.system(discord_path)
    bot.send_message(message.chat.id, '✅ Discord включен!')

def terminate_process_tree(pid):
    try:
        parent = psutil.Process(pid)
    except psutil.NoSuchProcess:
        return
    children = parent.children(recursive=True)
    for child in children:
        try:
            child.terminate()
        except psutil.NoSuchProcess:
            continue
    _, alive = psutil.wait_procs(children, timeout=3)
    for child in alive:
        try:
            child.kill()
        except psutil.NoSuchProcess:
            continue
    parent.terminate()
    try:
        parent.wait(timeout=3)
    except psutil.TimeoutExpired:
        parent.kill()

def turn_off_discord(message):
    # Флаг для отслеживания состояния процесса DiscordPTB
    discord_found = False
    
    # Выведем список всех процессов для отладки
    for proc in psutil.process_iter(['pid', 'name']):
        print(proc.info)  # Отладочный вывод, вы можете использовать логирование
    
    # Находим процесс по имени
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'DiscordPTB.exe':
            discord_found = True
            try:
                proc.terminate()  # Завершаем процесс
                proc.wait(timeout=3)  # Ожидаем завершения процесса
                bot.send_message(message.chat.id, '✅ DiscordPTB выключен!')
                return
            except psutil.TimeoutExpired:
                proc.kill()  # Принудительно завершаем процесс
                bot.send_message(message.chat.id, '✅ DiscordPTB принудительно выключен!')
                return
    
    if not discord_found:
        bot.send_message(message.chat.id, '❌ DiscordPTB не запущен.')

def turn_on_telegram(message):
    telegram_path = PROGRAM_PATHS['Telegram']
    subprocess.Popen(telegram_path)
    bot.send_message(message.chat.id, '✅ Telegram включен!')

def turn_off_telegram(message):
    for proc in psutil.process_iter(['pid', 'name']):
        if 'Telegram.exe' in proc.info['name']:
            pid = proc.info['pid']
            process = psutil.Process(pid)
            process.terminate()
            bot.send_message(message.chat.id, '✅ Telegram выключен!')
            return
    bot.send_message(message.chat.id, '❌ Telegram не запущен.')