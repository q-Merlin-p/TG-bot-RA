import pyautogui
from .errorLogger import log_activity, logger

def execute_keyboard_command(command_string):
    """
    Parses and executes a keyboard command.
    Supported formats:
    1. Repetition: "key * n" (e.g., "w * 3")
    2. Combination: "key1 + key2" (e.g., "ctrl + v")
    3. Typing: "text" (e.g., "Hello world")
    """
    try:
        command_string = command_string.strip()
        
        # Check for repetition (e.g., "w * 3")
        if '*' in command_string and len(command_string.split('*')) == 2:
            parts = command_string.split('*')
            key = parts[0].strip()
            try:
                count = int(parts[1].strip())
                pyautogui.press(key, presses=count)
                return f"Нажата клавиша '{key}' {count} раз(а)."
            except ValueError:
                pass # Not a valid integer, proceed to other checks

        # Check for combination (e.g., "ctrl + v")
        if '+' in command_string:
            keys = [k.strip() for k in command_string.split('+')]
            pyautogui.hotkey(*keys)
            return f"Выполнена комбинация: {' + '.join(keys)}"

        # Default: Type the string or press single key
        # If it's a known single key name, press it, otherwise typewrite
        if command_string in pyautogui.KEYBOARD_KEYS:
             pyautogui.press(command_string)
             return f"Нажата клавиша: {command_string}"
        else:
            pyautogui.write(command_string)
            return f"Напечатано: {command_string}"

    except Exception as e:
        logger.error(f"Error executing keyboard command: {e}")
        return f"Ошибка выполнения: {e}"
