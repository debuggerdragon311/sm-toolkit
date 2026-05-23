import unittest
from sm_core import count_occurrences, predecessor

class MyTestCase(unittest.TestCase):
    def test_array_utils(self):

        arr1: list[int] = [1, 0, 5, 4, 4]

        self.assertEqual(predecessor(arr1, 0), 1)
        self.assertEqual(count_occurrences(sorted(arr1), 1),1)


if __name__ == '__main__':
    unittest.main()
