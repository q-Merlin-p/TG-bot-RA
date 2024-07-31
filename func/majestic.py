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

def turn_on_MLauncer(message):
    majestic_path = PROGRAM_PATHS['MajesticLauncher']
    pyautogui.moveTo(x=1000, y=530, duration=1)
    print("Курсор выставлен на x=1000, y=530")

    launcher_thread = threading.Thread(target=launch_majestic_launcher, args=(majestic_path, message))
    launcher_thread.start()
    bot.send_message(message.chat.id, '🎮 Majestic включен! 🎮')

def launch_majestic_launcher(path, message):
    process = subprocess.Popen(path)
    print("Majestic лаунчер запущен")
    after_launcher_actions(message)

def after_launcher_actions(message):
    time.sleep(5)
    pyautogui.click()
    print("Дополнительные действия выполнены")
    bot.send_message(message.chat.id, '🎮 Вы начали подключаться к серверу!🎮')