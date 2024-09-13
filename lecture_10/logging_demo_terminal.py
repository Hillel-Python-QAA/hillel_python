import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logging.getLogger("").addHandler(console_handler)

logging.debug("This is DEBUG message")  # 10
logging.info("This is INFO message")  # 20
logging.warning("This is WARNING message")  # 30
logging.error("This is ERROR message")  # 40
logging.critical("This is CRITICAL message")  # 50
