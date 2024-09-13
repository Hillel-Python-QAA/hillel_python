import unittest

import pytest

from lecture_09.app import Calculator


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setup class")
        cls.calc = Calculator()

    def setUp(self):
        self._calc = Calculator()
        print("setup")

    def test_add_positive_values(self):
        print("id of a Class instance", id(self._calc))
        self.assertEqual(9, self._calc.add(4, 5))

    @unittest.skipIf(pytest.__version__ == "8.1.1", "pytest skipping")
    def test_add_negative_values(self):
        print("id of a Class instance", id(self._calc))
        self.assertEqual(
            -9,
            self._calc.add(-4, -5),
            msg="Test is Failed. Result is not equal to the expected one.",
        )


if __name__ == "__main__":
    unittest.main()
