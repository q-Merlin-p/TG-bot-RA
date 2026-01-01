import pyautogui
from .errorLogger import log_activity, logger

def move_cursor_to(x, y):
    try:
        pyautogui.moveTo(x, y)
        return True, f"Курсор перемещен на {x}, {y}"
    except Exception as e:
        logger.error(f"Error moving cursor: {e}")
        return False, f"Ошибка перемещения: {e}"

def click_mouse(button='left'):
    try:
        # pyautogui accepts 'left', 'middle', 'right', 'primary', 'secondary'
        if button not in ['left', 'right', 'middle']:
            return False, "Неверная кнопка мыши"
        
        pyautogui.click(button=button)
        return True, f"Нажата кнопка: {button}"
    except Exception as e:
        logger.error(f"Error clicking mouse: {e}")
        return False, f"Ошибка клика: {e}"

def get_mouse_position():
    return pyautogui.position()
