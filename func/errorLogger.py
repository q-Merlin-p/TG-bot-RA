import logging
import traceback

def is_logger_active(logger):
    return bool(logger.handlers)

logger = logging.getLogger('my_logger')
logger.setLevel(logging.ERROR)  
file_handler = logging.FileHandler('errors.txt')
file_handler.setLevel(logging.ERROR) 
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logging.basicConfig(
    filename='bot_activity.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8')

def log_activity(message, action):
    logging.info(f"User ID: {message.chat.id}, Action: {action}, Message: {message.text if hasattr(message, 'text') else 'N/A'}")

def log_message(message):
    sms_content = message.text if hasattr(message, 'text') else 'N/A'
    logging.info(f"SMS received - User ID: {message.chat.id}, Message: {sms_content}")
