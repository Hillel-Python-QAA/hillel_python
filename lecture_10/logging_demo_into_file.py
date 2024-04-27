import logging


logging.basicConfig(filename='example.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


logging.debug('This is DEBUG message')
logging.info('This is INFO message')
logging.warning('This is WARNING message')
logging.error('This is ERROR message')
logging.critical('This is CRITICAL message')


def add(a, b):
    logging.info(f'Adding two numbers {a} + {b}')
    return a+b


if __name__ == "__main__":
    print(add(2, 3))
