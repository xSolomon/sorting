''' Tests for lesson 8 solution. '''

import unittest
from sorting8_1 import MergeSort

class KthOrderStatisticsStepTests(unittest.TestCase):
    ''' Tests for KthOrderStatisticsStepTests function. '''
    def test_on_empty_array(self) -> None:
        ''' Array shouldn't change. '''
        values : list[int] = []
        self.assertEqual(MergeSort(values), values)

    def test_on_one_element_array(self) -> None:
        ''' Array shouldn't change. '''
        values : list[int] = [9]
        self.assertEqual(MergeSort(values), values)

    def test_on_predefined_arrays(self) -> None:
        ''' Each array should be sorted as the result. '''
        unsorted_arrays : list[list[int]] = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            [-525215, 1221, 677, 0, 111111, 32233, -6645332, 11343224, -2323523525252, 14141426474858],
            [0],
            [1, 2],
            [2, 1]
        ]
        for array in unsorted_arrays:
            sorted_array : list[int] = sorted(array)
            with self.subTest():
                self.assertEqual(MergeSort(array), sorted_array)

unittest.main()
