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

def lauch_rust(message):
    rust_path = PROGRAM_PATHS['RUST']
    os.system(rust_path)
    bot.send_message(message.chat.id, '🎮 вы запустили Rust...  🎮')