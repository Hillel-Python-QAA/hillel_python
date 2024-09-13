from loguru import logger


# logger.add(sys.stdout, format="{time} {level} {message}", level="INFO")
logger.add("loguru_log.txt")

logger.info("This is INFO message from loguru")
logger.debug("This is DEBUG message from loguru")
logger.warning("This is WARNING message from loguru")
logger.error("This is ERROR message from loguru")
logger.critical("This is CRITICAL message from loguru")


@logger.catch
def function(x, y, z):
    return 1 / (x + y + z)


function(2, 3, 2)
