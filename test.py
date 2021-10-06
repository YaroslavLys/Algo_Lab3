import unittest
from solution import Hamster


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        input_file_1 = "hamsters_in_test1.txt"
        self.assertEqual(Hamster.find_number_of_hamsters(input_file_1), 2)

    def test_case_2(self):
        input_file_2 = "hamsters_in_test2.txt"
        self.assertEqual(Hamster.find_number_of_hamsters(input_file_2), 3)

    def test_case_3(self):
        input_file_3 = "hamsters_in_test3.txt"
        self.assertEqual(Hamster.find_number_of_hamsters(input_file_3), 1)
