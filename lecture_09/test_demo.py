import unittest


def sum_function(a, b):
    if type(a) is str and type(b) is not str:
        b = str(b)
    return a + b


class MyTest(unittest.TestCase):
    def test_example(self):
        result = sum_function(4, 5)
        self.assertEqual(9, result)

    def test_sum_two_strings(self):
        result = sum_function("4", "5")
        self.assertEqual("45", result)

    def test_concatenation_int(self):
        actual_result = sum_function("4", 5)
        self.assertEqual("45", actual_result)

    def test_concatenation_float(self):
        actual_result = sum_function("4", 5.5)
        self.assertEqual("45.5", actual_result)

    # def test_type_error_on_attempt_concatenate_int(self):
    #     with self.assertRaises(TypeError):
    #         sum_function('4', 5)

    def test_sum_lists(self):
        actual_result = sum_function([1, 2, 3], [4, 5, 6])
        print("AR:", actual_result)
        self.assertEqual([1, 2, 3, 4, 5, 6], actual_result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
