''' Tests for lesson 2 solution. '''

import unittest
from typing import Tuple
from sorting2_1 import InsertionSortStep

class InsertionSortStepTests(unittest.TestCase):
    ''' Tests for InsertionSortStep function. '''
    def test_on_seven_element_array(self) -> None:
        ''' Results for each argument list must be
            same as expected. '''
        args_and_results : list[Tuple(Tuple(list[int], int, int), list[int])] = [
            (([1, 6, 5, 4, 3, 2, 7], 3, 1), [1, 3, 5, 4, 6, 2, 7]),
            (([1, 6, 5, 4, 3, 2, 7], 1, 0), [1, 2, 3, 4, 5, 6, 7]),
            (([7, 6, 5, 4, 3, 2, 1], 3, 0), [1, 6, 5, 4, 3, 2, 7]),
            (([1, 6, 5, 4, 3, 2, 7], 3, 1), [1, 3, 5, 4, 6, 2, 7]),
            (([1, 3, 5, 4, 6, 2, 7], 3, 2), [1, 3, 2, 4, 6, 5, 7]),
            (([1, 3, 2, 4, 6, 5, 7], 3, 3), [1, 3, 2, 4, 6, 5, 7]),
        ]
        for test_data in args_and_results:
            test_input : Tuple(list[int], int, int) = test_data[0]
            test_output : list[int] = test_data[1]
            with self.subTest():
                InsertionSortStep(*test_input)
                self.assertEqual(test_input[0], test_output)

unittest.main()
