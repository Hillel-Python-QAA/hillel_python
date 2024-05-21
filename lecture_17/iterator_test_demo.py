import unittest


def my_sort(arr):
    return sorted(arr)


class TestSortFunction(unittest.TestCase):
    def test_sorting(self):
        test_data = [
            ([3, 2, 1], [1, 2, 3]),
            ([5, 1, 4, 2], [1, 2, 4, 5]),
        ]

        for input_arr, expected_output in test_data:
            with self.subTest(input_arr=input_arr):
                self.assertEqual(my_sort(input_arr), expected_output)


if __name__ == "__main__":
    unittest.main()
