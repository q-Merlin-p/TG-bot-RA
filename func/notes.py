# notes.py
import json
import telebot

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    notes_file = config['notes_file']

def load_notes():
    try:
        with open(notes_file, 'r', encoding='utf-8') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []  # Если файл отсутствует, начинаем с пустого списка
    if not isinstance(notes, list):
        notes = []  # Если загруженный объект не является списком, начинаем с пустого списка
    return notes

def save_notes(notes):
    with open(notes_file, 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)

def new_note_command(message, bot):
    bot.reply_to(message, "Отлично! Введи заголовок новой заметки:")
    bot.register_next_step_handler(message, process_title_step, bot)

def process_title_step(message, bot):
    chat_id = message.chat.id
    title = message.text
    bot.send_message(chat_id, f"Отлично! Заголовок заметки: {title}. Теперь введи содержимое заметки:")
    bot.register_next_step_handler(message, process_content_step, title, bot)

def process_content_step(message, title, bot):
    chat_id = message.chat.id
    content = message.text

    new_note = {
        'title': title,
        'content': content
    }

    notes = load_notes()
    notes.append(new_note)
    save_notes(notes)
    bot.send_message(chat_id, "Заметка успешно создан!")

def view_notes_command(call, bot):
    notes = load_notes()
    if notes:
        for i, note in enumerate(notes):
            markup = telebot.types.InlineKeyboardMarkup()
            markup.row(
                telebot.types.InlineKeyboardButton("🗑️ Удалить заметку", callback_data=f'delete_note_{i}'),
                telebot.types.InlineKeyboardButton("✏️ Редактировать заметку", callback_data=f'edit_note_{i}')
            )
            bot.send_message(call.message.chat.id, f"📌 <b>{note['title']}</b>\n{note['content']}", parse_mode='HTML', reply_markup=markup)
    else:
        bot.send_message(call.message.chat.id, "❌ Нет доступных заметок.")

def delete_note_command(call, bot):
    note_index = int(call.data.split('_')[2])
    notes = load_notes()
    if 0 <= note_index < len(notes):
        deleted_note = notes.pop(note_index)
        save_notes(notes)
        bot.send_message(call.message.chat.id, f"✅ Заметка '{deleted_note['title']}' успешно удалена!")
    else:
        bot.send_message(call.message.chat.id, "❌ Не удалось удалить заметку. Попробуйте снова.")

def edit_note_command(call, bot):
    note_index = int(call.data.split('_')[2])
    notes = load_notes()
    if 0 <= note_index < len(notes):
        bot.send_message(call.message.chat.id, f"Редактирование заметки: {notes[note_index]['title']}\nВведите новый заголовок:")
        bot.register_next_step_handler(call.message, process_edit_title_step, note_index, bot)
    else:
        bot.send_message(call.message.chat.id, "❌ Не удалось редактировать заметку. Попробуйте снова.")

def process_edit_title_step(message, note_index, bot):
    chat_id = message.chat.id
    new_title = message.text
    bot.send_message(chat_id, f"Отлично! Новый заголовок: {new_title}. Теперь введи новое содержимое:")
    bot.register_next_step_handler(message, process_edit_content_step, note_index, new_title, bot)

def process_edit_content_step(message, note_index, new_title, bot):
    chat_id = message.chat.id
    new_content = message.text

    notes = load_notes()
    if 0 <= note_index < len(notes):
        notes[note_index]['title'] = new_title
        notes[note_index]['content'] = new_content
        save_notes(notes)
        bot.send_message(chat_id, "Заметка успешно обновлена!")
    else:
        bot.send_message(chat_id, "❌ Не удалось обновить заметку. Попробуйте снова.")