# 🖥️ Telegram Remote Access Bot

**Назначение:**  
Позволяет управлять локальной машиной через Telegram-бота. Поддерживает выполнение системных команд, взаимодействие с экраном, процессами и файловой системой.

---

## 📦 Зависимости

Минимальные зависимости (Python 3.9+):

```bash
pip install telebot pyautogui psutil Pillow pyperclip
````

### Используемые библиотеки:

| Библиотека         | Назначение                            |
| ------------------ | ------------------------------------- |
| `telebot` | Telegram Bot API                               |
| `pyautogui`        | Управление экраном и мышью, скриншоты |
| `psutil`           | Информация о процессах и системе      |
| `Pillow`           | Обработка изображений                 |
| `pyperclip`        | Доступ к буферу обмена                |

---

## ⚙️ Принцип работы

1. **Инициализация бота**:

   * Чтение `config.json` (токен, авторизованные ID).
   * Настройка обработчиков сообщений в `sss.py`.

2. **Обработка входящих сообщений**:

   * Каждое сообщение проверяется на валидность ID отправителя.
   * По содержимому сообщения определяется команда и соответствующий модуль для её обработки.

3. **Вызов логики из модулей**:

   * Все команды разнесены по файлам в директории `func/`.
   * Обработка происходит через `import func.<module>`.

4. **Логирование**:

   * Все действия пишутся в `bot_activity.log`.
   * Ошибки фиксируются в `errors.txt`.

5. **Ответ пользователю**:

   * Результат выполнения команды отправляется в Telegram-чат.

---

## 📁 Структура проекта

```text
TG-bot-RA/
├── func/                    # Каталог с логикой команд (вспомогательные модули)
│   ├── __init__.py
│   ├── screen.py            # Скриншоты экрана
│   ├── cmd.py               # Выполнение команд оболочки
│   ├── clipboard.py         # Работа с буфером обмена
│   └── ...                  # Прочие модули (аудио, управление окнами, и т.п.)
│
├── sss.py                   # Главный файл, запускающий бота и обрабатывающий команды
├── starter.bat              # Скрипт для автозапуска под Windows
├── config.json              # Конфигурационный файл с токеном и ID владельца
├── notes.json               # Служебные данные для некоторых функций
├── bot_activity.log         # Лог команд и активности
├── errors.txt               # Лог ошибок
└── README.md                # Документация (вы здесь!)
```

---

## 🧩 Компоненты и логика

### 1. Конфигурация

`config.json`:

```json
{
  "token": "YOUR_TELEGRAM_BOT_TOKEN",
  "owner_id": 123456789,
  "trusted_users": [123456789, 987654321]
}
```

Используется при инициализации для авторизации пользователей.

---

### 2. Объявление команд

Происходит в `sss.py`, вручную через `if-elif` или `match-case` (в новых версиях Python). Пример:

```python
if message.text.startswith('/screenshot'):
    from func import screen
    screen.capture_and_send(bot, message)
```

---

### 3. Модули команд

Все модули находятся в папке `func/`, каждый реализует конкретную задачу:

* `screen.py` — создание скриншота, отправка пользователю.
* `cmd.py` — выполнение shell-команд, возврат вывода.
* `clipboard.py` — получить/установить содержимое буфера обмена.
* `processes.py` — работа с запущенными процессами.
* `system.py` — информация о CPU, памяти, температуре и т.п.

Каждый модуль содержит одну или несколько функций вида `execute(bot, message)` или специализированных `handle_<cmd>()`.

---

## 🧪 Пример команды

Входящее сообщение от Telegram:

```text
/cmd dir C:\
```

**Обработка:**

* Проверка прав доступа (`owner_id`)
* Парсинг команды: `cmd`, аргумент: `dir C:\`
* Импорт `func.cmd`, вызов `run_command("dir C:\")`
* Возврат результата через `bot.send_message(...)`

---

## 🔐 Безопасность

> ⚠️ В текущем виде бот рассчитан на **локальное использование** или работу в доверенной сети/группе.
> Для продакшн-сценариев стоит внедрить:

* Хэширование команд
* Жесткий список разрешённых операций
* Шифрование и аутентификация
* Обфускация исходного кода

---
