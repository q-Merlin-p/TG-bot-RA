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