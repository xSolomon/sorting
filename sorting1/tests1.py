''' Tests for lesson 1 solution. '''

import unittest
from sorting1_1 import SelectionSortStep, BubbleSortStep

class SelectionSortStepTests(unittest.TestCase):
    ''' Tests for SelectionSortStep function. '''
    def test_on_sorted_array(self) -> None:
        ''' Expected nothing changed. '''
        values : list[int] = [i for i in range(10)]
        for i, _ in enumerate(values):
            with self.subTest():
                SelectionSortStep(values, i)
                self.assertEqual(values, [x for x in range(10)])

    def test_on_fully_unsorted_array(self) -> None:
        ''' Expected fully sorted array after n function runs. '''
        values : list[int] = list(reversed(range(10)))
        for i in range(10):
            with self.subTest():
                SelectionSortStep(values, i)
        self.assertEqual(values, [i for i in range(10)])

class BubbleSortStepTests(unittest.TestCase):
    ''' Tests for BubbleSortStep function. '''
    def test_on_sorted_array(self) -> None:
        ''' Expected nothing changed, function returns false. '''
        values : list[int] = [i for i in range(10)]
        self.assertFalse(BubbleSortStep(values))
        self.assertEqual(values, [i for i in range(10)])

    def test_on_fully_unsorted_array(self) -> None:
        ''' Expected n - 1 swaps, function returns true. '''
        values : list[int] = list(reversed(range(10)))
        for i in range(9):
            with self.subTest(i = i):
                self.assertTrue(BubbleSortStep(values))
        self.assertEqual(values, [i for i in range(10)])

    def test_on_predefined_array(self) -> None:
        ''' Expected sorted array after 2 steps. '''
        values : list[int] = [4, 3, 1, 2]
        self.assertTrue(BubbleSortStep(values))
        self.assertEqual(values, [3, 1, 2, 4])
        self.assertTrue(BubbleSortStep(values))
        self.assertEqual(values, [1, 2, 3, 4])
        self.assertFalse(BubbleSortStep(values))

unittest.main()
