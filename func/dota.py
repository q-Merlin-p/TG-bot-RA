import telebot
import json
import os
import psutil
import pyautogui
import time

from .errorLogger import logger

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    API_TOKEN = config['API_TOKEN']
    ALLOWED_USERS = config['ALLOWED_USERS']
    PROGRAM_PATHS = config['PROGRAM_PATHS']

bot = telebot.TeleBot(API_TOKEN)

def launch_dota_two(message):
    dota_path = PROGRAM_PATHS['Dota2']
    os.system(dota_path)
    bot.send_message(message.chat.id, '🎮 вы запустили Dota 2! 🎮')

def exet_dota(message):
    try:
        process_name = 'dota2.exe'  # Замените на правильное имя процесса
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'].lower() == process_name.lower():
                proc.terminate()
                bot.send_message(message.chat.id, '❌ Вы завершили процесс Dota 2')
                return
        bot.send_message(message.chat.id, 'Процесс Dota 2 не найден.')
    except Exception as e:
        if logger:
            logger.error(f'Ошибка в exet_dota: {str(e)}', exc_info=True)
        bot.send_message(message.chat.id, f'❌ Произошла ошибка: {str(e)}')

def accept_game(message):
    pyautogui.moveTo(x=951, y=365, duration=1)
    pyautogui.click()
    bot.send_message(message.chat.id, '🎮 вы приняли игру Dota 2! 🎮')

def pick_hero(message):
    pyautogui.moveTo(x=1100, y=230, duration=1)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(x=1400, y=830, duration=1)
    pyautogui.click()
    bot.send_message(message.chat.id, 'Вы пикнули СФА')

def pick_hero_rez(message):
    pyautogui.moveTo(x=1110, y=230, duration=1)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(x=1400, y=830, duration=1)
    pyautogui.click()
    bot.send_message(message.chat.id, 'Вы пикнули Мортру')

def ban_hero(message):
    pyautogui.moveTo(x=1070, y=430, duration=1)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(x=1400, y=740, duration=1)
    pyautogui.click()
    bot.send_message(message.chat.id, 'Вы забанили героя')