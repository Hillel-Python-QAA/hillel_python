import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.StreamHandler(),
                        logging.FileHandler('example_code.log')
                    ])


logger = logging.getLogger(__name__)

logger.debug('This is DEBUG message')
logger.info('This is INFO message')
