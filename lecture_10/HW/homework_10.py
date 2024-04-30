"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import unittest


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """

    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='lecture_10/HW/login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
        )

    logger = logging.getLogger('log_event')

    # # Логування події
    # if status == "success":
    #     logger.info(log_message)
    # elif status == "expired":
    #     logger.warning(log_message)
    # else:
    #     logger.error(log_message)

    match status:
        case 'success':
            logger.info(log_message)
        case 'expired':
            logger.warning(log_message)
        case _:
            logger.error(log_message)
