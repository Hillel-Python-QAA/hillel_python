import unittest
from lecture_09.test_demo import MyTest
from lecture_09.test_calc import MyTestCase


def suite():
    _suite = unittest.TestSuite()
    _suite.addTest(MyTest("test_example"))
    _suite.addTest(MyTest("test_sum_two_strings"))
    _suite.addTest(MyTest("test_concatenation_int"))
    _suite.addTest(MyTest("test_concatenation_float"))
    _suite.addTest(MyTest("test_sum_lists"))
    _suite.addTest(MyTestCase("test_add_negative_values"))
    _suite.addTest(MyTestCase("test_add_positive_values"))
    return _suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
