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

def launch_FIREFOX(message):
    FIREFOX_path = PROGRAM_PATHS['FIREFOX']
    command = f'"{FIREFOX_path}"'
    subprocess.run(command, shell=True)
    bot.send_message(message.chat.id, '🦊 FIREFOX был запущён')