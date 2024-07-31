import telebot
import tempfile
import json
from PIL import ImageGrab 
import os
import psutil
import webbrowser
import pyautogui
import subprocess
import time
import threading
import psutil

from .dota import launch_dota_two, exet_dota, accept_game, pick_hero, pick_hero_rez, ban_hero
from .steam import launch_steam, start_steam, complete_steam_launch
from .rust import lauch_rust
from .vsc import launch_vsc
from .FireFox import launch_FIREFOX
from .majestic import turn_on_MLauncer, launch_majestic_launcher, after_launcher_actions
from .messengers import turn_on_discord, turn_off_discord, turn_on_telegram, turn_off_telegram
from .browser import open_url, get_url_from_action
from .sendtime import send_uptime, format_uptime
from .sleep import sleep_computer
from .record import press_pause_button
from .tvers import get_telebot_version 
from .errorLogger import is_logger_active, logger
from .notes import new_note_command, delete_note_command, view_notes_command, load_notes, save_notes, edit_note_command, process_edit_title_step, process_edit_content_step


