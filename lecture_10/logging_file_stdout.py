import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logfile.txt')

console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s - %(filename)s - %(funcName)s - %(lineno)d - %(name)s',
    datefmt='%Y-%m-%d %H:%M:%S')

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def run_logger():
    logger.debug('This is DEBUG message')  # 10
    logger.info('This is INFO message')  # 20
    logger.warning('This is WARNING message')  # 30
    logger.error('This is ERROR message')  # 40
    logger.critical('This is CRITICAL message')  # 50


run_logger()

file_handler.close()
