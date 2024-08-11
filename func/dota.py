import telebot
import json
import os
import psutil
import pyautogui
import time

from .errorLogger import logger,log_activity

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    API_TOKEN = config['API_TOKEN']
    ALLOWED_USERS = config['ALLOWED_USERS']
    PROGRAM_PATHS = config['PROGRAM_PATHS']

bot = telebot.TeleBot(API_TOKEN)


def launch_dota_two(message):
    log_activity(message, "Launch Dota 2")
    logger.info(f"User ID: {message.chat.id}, Action: Launch Dota 2")
    dota_path = PROGRAM_PATHS['Dota2']
    os.system(dota_path)
    bot.send_message(message.chat.id, '🎮 вы запустили Dota 2! 🎮')

def exet_dota(message):
    log_activity(message, "Exit Dota 2")
    logger.info(f"User ID: {message.chat.id}, Action: Exit Dota 2")
    try:
        process_name = 'dota2.exe'
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'].lower() == process_name.lower():
                proc.terminate()
                bot.send_message(message.chat.id, '❌ Вы завершили процесс Dota 2')
                return
        bot.send_message(message.chat.id, 'Процесс Dota 2 не найден.')
    except Exception as e:
        logger.error(f'Ошибка в exet_dota: {str(e)}', exc_info=True)
        bot.send_message(message.chat.id, f'❌ Произошла ошибка: {str(e)}')

def accept_game(message):
    log_activity(message, "Accept Game")
    logger.info(f"User ID: {message.chat.id}, Action: Accept Game")
    pyautogui.moveTo(x=951, y=365)
    pyautogui.click()
    bot.send_message(message.chat.id, '🎮 вы приняли игру Dota 2! 🎮')

def pick_hero(message):
    log_activity(message, "Pick Hero (SF)")
    logger.info(f"User ID: {message.chat.id}, Action: Pick Hero (SF)")
    pyautogui.moveTo(x=1100, y=230)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(x=1400, y=830)
    pyautogui.click()
    bot.send_message(message.chat.id, 'Вы пикнули СФА')

def pick_hero_rez(message):

    log_activity(message, "Pick Hero (Mortra)")
    logger.info(f"User ID: {message.chat.id}, Action: Pick Hero (Mortra)")

    pyautogui.moveTo(x=1110, y=230)
    pyautogui.click()

    time.sleep(0.2)

    pyautogui.moveTo(x=1400, y=830)
    pyautogui.click()

    bot.send_message(message.chat.id, 'Вы пикнули Мортру')

def ban_hero(message):
    log_activity(message, "Ban Hero")
    logger.info(f"User ID: {message.chat.id}, Action: Ban Hero")
    pyautogui.moveTo(x=1070, y=430)
    pyautogui.click()
    bot.send_message(message.chat.id, 'Вы забанили героя.')