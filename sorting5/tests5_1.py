''' Tests for lesson 5 solution. '''

import unittest
from sorting5_1 import partition, QuickSort

class PartitionTests(unittest.TestCase):
    ''' Tests for partition function. '''
    def test_on_empty_array(self) -> None:
        ''' Expected None as pivot, array shouldn't change. '''
        values : list[int] = []
        self.assertIsNone(partition(values, 0, 0))
        self.assertEqual(values, [])

    def test_on_seven_elements_array(self) -> None:
        ''' Expected correct pivot and changes to array. '''
        values : list[int] = [7, 5, 6, 4, 3, 1, 2]
        results : tuple[int, list[int]] = (3, [2, 1, 3, 4, 6, 5, 7])
        with self.subTest():
            self.assertEqual(partition(values, 0, len(values) - 1), results[0])
            self.assertEqual(values, results[1])
        values = [1, 3, 4, 6, 5, 2, 8]
        results = (5, [1, 3, 4, 2, 5, 6, 8])
        with self.subTest():
            self.assertEqual(partition(values, 0, len(values) - 1), results[0])
            self.assertEqual(values, results[1])

class QuickSortTests(unittest.TestCase):
    ''' Tests for QuickSort function. '''
    def test_on_empty_array(self) -> None:
        ''' Array shouldn't change. '''
        values : list[int] = []
        QuickSort(values, 0, len(values) - 1)
        self.assertEqual(values, [])

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
                QuickSort(array, 0 , len(array) - 1)
                self.assertEqual(array, sorted_array)

unittest.main()
