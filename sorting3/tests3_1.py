''' Tests for lesson 3 solution. '''

import unittest
from typing import Tuple
from sorting3_1 import KnuthSequence

class KnuthSequenceTests(unittest.TestCase):
    ''' Tests for KnuthSequence function. '''
    def test_on_empty_array(self) -> None:
        ''' Must return an empty list. '''
        self.assertEqual(KnuthSequence(0), [])

    def test_for_predefined_array_sizes(self) -> None:
        ''' For each size must return expected sequence. '''
        tests_data : list[Tuple(int, list[int])] = [
            (1, [1]),
            (12, [4, 1]),
            (13, [13, 4, 1]),
            (14, [13, 4, 1]),
            (365, [364, 121, 40, 13, 4, 1])
        ]
        for test_data in tests_data:
            with self.subTest():
                self.assertEqual(KnuthSequence(test_data[0]), test_data[1])

unittest.main()
