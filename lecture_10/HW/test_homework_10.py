"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import os.path
import unittest

from lecture_10.HW.homework_10 import log_event


class TestLogEvent(unittest.TestCase):
    def test_log_event_creates_file(self):
        log_event("user", "success")
        self.assertTrue(os.path.isfile("lecture_10/HW/login_system.log"))

    def test_log_event(self):
        with self.assertLogs("log_event", level="INFO") as logger:
            log_event("user", "success")
            log_event("user", "expired")
            log_event("user", "error")
        self.assertEqual(
            logger.output,
            [
                "INFO:log_event:Login event - Username: user, Status: success",
                "WARNING:log_event:Login event - Username: user, Status: expired",
                "ERROR:log_event:Login event - Username: user, Status: error",
            ],
        )

    def test_log_event_success(self):
        with self.assertLogs("log_event", level="INFO") as logger:
            log_event("user", "success")
        self.assertEqual(
            logger.output,
            ["INFO:log_event:Login event - Username: user, Status: success"],
        )

    def test_log_event_expired(self):
        with self.assertLogs("log_event", level="WARNING") as logger:
            log_event("user", "expired")
        self.assertEqual(
            logger.output,
            ["WARNING:log_event:Login event - Username: user, Status: expired"],
        )

    def test_log_event_error(self):
        with self.assertLogs("log_event", level="ERROR") as logger:
            log_event("user", "error")
        self.assertEqual(
            logger.output,
            ["ERROR:log_event:Login event - Username: user, Status: error"],
        )


if __name__ == "__main__":
    # log_event('user', 'success')
    unittest.main()
