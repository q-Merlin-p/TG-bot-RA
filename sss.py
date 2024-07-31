import telebot
import tempfile
import json
from PIL  import ImageGrab 
import os
import pyautogui
from colorama import init, Fore, Style
from func.functions import *

init()

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    API_TOKEN = config['API_TOKEN']
    ALLOWED_USERS = config['ALLOWED_USERS']
    PROGRAM_PATHS = config['PROGRAM_PATHS']
    notes_file = config['notes_file']
    botVersion = config['botVersion']
    dataUpdate = config['dataUpdate']

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("Получена команда /start")
    print("ID пользователя, отправившего сообщение:", message.chat.id)
    print("ID разрешенных пользователей:", ALLOWED_USERS)
    if message.chat.id in ALLOWED_USERS:
        markup = start_menu_markup()
        bot.send_message(message.chat.id, '👋 Добро пожаловать!', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, '❌ Извините, у вас нет разрешения использовать этого бота.')

def start_menu_markup():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("💻Другие действия💻","🎮 Программы 🎵","🎮 Дота 2🃏")
    markup.add("💬 Заметки","🗨️ Общение","🌐 Браузер")
    return markup

@bot.message_handler(regexp='Заметки')
def note(message):
    if message.chat.id in ALLOWED_USERS:
        markup = note_actions_markup()
        bot.send_message(message.chat.id, '🗨️ Управление:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, '❌ Извините, у вас нет разрешения использовать этого бота.')

def note_actions_markup():
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(telebot.types.InlineKeyboardButton("📝 Создать заметку", callback_data='new_note_command'))
    markup.row(telebot.types.InlineKeyboardButton("📖 Просмотр заметок", callback_data='view_notes_command'))
    
    return markup

@bot.message_handler(commands=['newnote'])
def handle_new_note_command(message):
    new_note_command(message, bot)

@bot.callback_query_handler(func=lambda call: call.data == 'view_notes_command')
def handle_view_notes_command(call):
    view_notes_command(call, bot)

@bot.callback_query_handler(func=lambda call: call.data.startswith('delete_note_'))
def handle_delete_note_command(call):
    delete_note_command(call, bot)

@bot.message_handler(regexp='другие действия')
def other_actions(message):
    if message.chat.id in ALLOWED_USERS:
        markup = other_actions_markup()
        bot.send_message(message.chat.id, '💻 Выберите действие:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, '❌ Извините, у вас нет разрешения использовать этого бота.')

def other_actions_markup():
    markup = telebot.types.InlineKeyboardMarkup()
    
    markup.row(
        telebot.types.InlineKeyboardButton("💤 Sleep Mode", callback_data='sleep'),
        telebot.types.InlineKeyboardButton("❌ OFF PC", callback_data='shutdown'),
        telebot.types.InlineKeyboardButton("🔄 Reboot PC", callback_data='reboot'))
    
    markup.row(
        telebot.types.InlineKeyboardButton("📸 Сделать скриншот", callback_data='take_screenshot'),
        telebot.types.InlineKeyboardButton("🎥 On/off Откат", callback_data='press_pause_button'))

    markup.row(telebot.types.InlineKeyboardButton("🔄 Альтаб 🔄", callback_data='alt_tab'))
    markup.row(telebot.types.InlineKeyboardButton("🧼 Очистка консоли",callback_data="cls"))
    markup.row(telebot.types.InlineKeyboardButton("🕒 Время работы ПК", callback_data='uptime'))
    return markup

@bot.message_handler(regexp='сделать скриншот')
def take_screenshot(message):
    if message.chat.id in ALLOWED_USERS:
        try:
            path = tempfile.gettempdir() + 'screenshot.png'
            screenshot = ImageGrab.grab()
            screenshot.save(path, 'PNG')
            bot.send_photo(message.chat.id, open(path, 'rb'))
            bot.send_message(message.chat.id, '📸 Скриншот отправлен!')
        except Exception as e:
            logger.error(f'Ошибка при создании скриншота: {str(e)}', exc_info=True)
            bot.send_message(message.chat.id, f'❌ Произошла ошибка: {str(e)}')
    else:
        bot.send_message(message.chat.id, '❌ Извините, у вас нет разрешения использовать этого бота.')


@bot.message_handler(regexp='Программы')
def other_actions(message):
    if message.chat.id in ALLOWED_USERS:
        markup = program_markup()
        bot.send_message(message.chat.id, '💻 Выберите програму:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, '❌ Извините, у вас нет разрешения использовать этого бота.')

def program_markup():
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(
        telebot.types.InlineKeyboardButton("🎮 Majestic", callback_data='turn_on_MLauncer'),
        telebot.types.InlineKeyboardButton("♨ steam",callback_data="launch_steam"),
        telebot.types.InlineKeyboardButton("☢ Rust", callback_data="lauch_rust"))
    markup.row(
        telebot.types.InlineKeyboardButton("👨🏼‍💻 VSC", callback_data="launch_vsc"),
        telebot.types.InlineKeyboardButton("🦊 Firefox", callback_data="launch_FIREFOX"))
    return markup

@bot.message_handler(regexp='Дота')
def chat(message):
    if message.chat.id in ALLOWED_USERS:
        markup = dota_actions_markup()
        bot.send_message(message.chat.id, '💻 Выберите действие по отношение к Доте:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, '❌ Извините, у вас нет разрешения использовать этого бота.')

def dota_actions_markup():
    markup = telebot.types.InlineKeyboardMarkup()

    markup.row(
        telebot.types.InlineKeyboardButton("🎮 Запуск доты",callback_data="launch_dota_two"),
        telebot.types.InlineKeyboardButton("❌ Выключение доты",callback_data="exet_dota"))

    markup.row(telebot.types.InlineKeyboardButton("🌊 Принять игру", callback_data="accept_game"))
    markup.row(telebot.types.InlineKeyboardButton("🩸 Забанить героя", callback_data="ban_hero"))

    markup.row(
        telebot.types.InlineKeyboardButton("🎃 Пик (SF)", callback_data="pick_hero"),
        telebot.types.InlineKeyboardButton("💀 Пик (PA)", callback_data="pick_hero_rez"))
    
    return markup 

@bot.message_handler(regexp='общение')
def chat(message):
    if message.chat.id in ALLOWED_USERS:
        markup = control_markup()
        bot.send_message(message.chat.id, '🗨️ Управление:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, '❌ Извините, у вас нет разрешения использовать этого бота.')

def control_markup():
    markup = telebot.types.InlineKeyboardMarkup()
    
    markup.row(
        telebot.types.InlineKeyboardButton("🟢 Включить Discord", callback_data='turn_on_discord'),
        telebot.types.InlineKeyboardButton("🔴 Выключить Discord", callback_data='turn_off_discord'))
    
    markup.row(
        telebot.types.InlineKeyboardButton("🟢 Включить Telegram", callback_data='turn_on_telegram'),
        telebot.types.InlineKeyboardButton("🔴 Выключить Telegram", callback_data='turn_off_telegram'))
    return markup

@bot.message_handler(regexp='браузер')
def open_browser(message):
    if message.chat.id in ALLOWED_USERS:
        markup = browser_markup()
        bot.send_message(message.chat.id, '🌐 Выберите сайт:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, '❌ Извините, у вас нет разрешения использовать этого бота.')

def browser_markup():
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton("🎥 Ютуб", callback_data='open_url_youtube'),
        telebot.types.InlineKeyboardButton("🎵 Музыка", callback_data='open_url_music'))
    
    markup.add(
        telebot.types.InlineKeyboardButton("🎞 Кино", callback_data='open_url_kino'),
        telebot.types.InlineKeyboardButton("📼 Сериалы",callback_data="open_url_serials"))

    markup.row(
        telebot.types.InlineKeyboardButton("🖼 Аниме", callback_data='open_url_anime'),
        telebot.types.InlineKeyboardButton("🐱‍👤 Аниме",callback_data="open_url_anime2"))

    markup.add(telebot.types.InlineKeyboardButton("📬 ChatGPT", callback_data='open_url_GPT'))
    markup.add(telebot.types.InlineKeyboardButton("☎ Nekto", callback_data='open_url_NEKTO'))

    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.message.chat.id in ALLOWED_USERS:
        action = call.data
        try:
            actions = {
                'new_note_command': lambda msg: new_note_command(msg, bot),
                'turn_on_discord': turn_on_discord,
                'turn_off_discord': turn_off_discord,
                'turn_on_telegram': turn_on_telegram,
                'turn_off_telegram': turn_off_telegram,
                'turn_on_MLauncer': turn_on_MLauncer,
                'launch_dota_two': launch_dota_two,
                'launch_steam': launch_steam,
                'launch_vsc': launch_vsc,
                'launch_FIREFOX': launch_FIREFOX,
                'lauch_rust': lauch_rust,
                'accept_game': accept_game,
                'ban_hero': ban_hero,
                'pick_hero': pick_hero,
                'pick_hero_rez': pick_hero_rez,
                'cls': lambda msg: (os.system('cls' if os.name == 'nt' else 'clear'),print(BotInfo), bot.send_message(msg.chat.id, '🧼 Консоль была очищена')),
                'alt_tab': lambda msg: (pyautogui.hotkey('alt', 'tab'), bot.send_message(msg.chat.id, '🔄 Вкладка сменилась')),
                'reboot': lambda msg: (bot.send_message(msg.chat.id, '🔄 Перезагружаю компьютер...'), os.system("shutdown -r -t 0")),
                'sleep': lambda msg: (bot.send_message(msg.chat.id, '💤 Перевожу компьютер в спящий режим...'), sleep_computer()),
                'shutdown': lambda msg: (bot.send_message(msg.chat.id, '❌ Выключаю компьютер...'), os.system("shutdown -s -t 0")),
                'take_screenshot': take_screenshot,
                'press_pause_button': press_pause_button,
                'uptime': send_uptime,
                'edit_note_command': lambda msg: edit_note_command(msg, bot)
            }

            if action.startswith('open_url_'):
                open_url(call.message, get_url_from_action(action))
            elif action.startswith('delete_note_'):
                delete_note_command(call, bot)
            elif action.startswith('edit_note_'):
                edit_note_command(call, bot)
            else:
                if action in actions:
                    actions[action](call.message)
                else:
                    bot.send_message(call.message.chat.id, '❌ Неизвестное действие.')
        except Exception as e:
            logger.error(f'Ошибка в callback_handler: {str(e)}', exc_info=True)
            bot.send_message(call.message.chat.id, f'❌ Произошла ошибка: {str(e)}')
    else:
        bot.send_message(call.message.chat.id, '❌ Извините, у вас нет разрешения использовать этого бота.')


bot.infinity_polling()