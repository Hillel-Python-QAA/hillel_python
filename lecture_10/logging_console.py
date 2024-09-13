import logging


logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()

console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

logger.debug("This is DEBUG message")  # 10
logger.info("This is INFO message")  # 20
logger.warning("This is WARNING message")  # 30
logger.error("This is ERROR message")  # 40
logger.critical("This is CRITICAL message")  # 50
