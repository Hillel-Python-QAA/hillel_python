import logging
import logging.config


logging.config.fileConfig('logging_config.ini')

logger = logging.getLogger('sampleLogger')


logger.debug('This is DEBUG message')
logger.info('This is INFO message')

