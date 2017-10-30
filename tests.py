from functions import sum_num, generate_list
import unittest


class TestSumAB(unittest.TestCase):

    def test_numbers_sum(self):
        self.assertEqual(sum_num(2, 3), 5)

    def test_generate_list(self):
        new_list = generate_list(1, 4, 5, 10)
        self.assertIsInstance(new_list, list)
        self.assertIn(4, new_list)
        self.assertIsNot(new_list, None)
        self.assertGreater(len(new_list), 0)
