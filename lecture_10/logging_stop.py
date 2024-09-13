import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)

logger.info("This is INFO message")

logging.shutdown()
