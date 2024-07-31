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

def launch_steam(message):
    steam_path = PROGRAM_PATHS['Steam']
    pyautogui.moveTo(x=700, y=530, duration=1)
    print("Курсор выставлен на x=700, y=530")

    steam_thread = threading.Thread(target=start_steam, args=(steam_path, message))
    steam_thread.start()

def start_steam(path, message):
    process = subprocess.Popen(path)
    print("Steam запущен")
    complete_steam_launch(message)

def complete_steam_launch(message):
    time.sleep(8)
    print("Слип 8 сек")
    pyautogui.click()
    print("Клик выполнен")
    bot.send_message(message.chat.id, '🎮 Steam был запущен! 🎮')