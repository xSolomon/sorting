''' Tests for lesson 5 solution. '''

import unittest
from sorting7_1 import KthOrderStatisticsStep

class KthOrderStatisticsStepTests(unittest.TestCase):
    ''' Tests for KthOrderStatisticsStepTests function. '''
    def test_on_empty_array(self) -> None:
        ''' Array shouldn't change. '''
        values : list[int] = []
        self.assertEqual(KthOrderStatisticsStep(values, 0, len(values) - 1, 0), [])

    def test_on_one_element_array(self) -> None:
        ''' Expected 0 for both borders when 0th order statistics asked.
            Expected empty list otherwise. '''
        values : list[int] = [9]
        self.assertEqual(KthOrderStatisticsStep(values, 0, len(values) - 1, 0), [0, 0])
        self.assertEqual(KthOrderStatisticsStep(values, 0, len(values) - 1, -1), [0, -1])
        self.assertEqual(KthOrderStatisticsStep(values, 0, len(values) - 1, 1), [1, 0])

    def test_on_seven_element_array(self) -> None:
        ''' Each array should be sorted as the result. '''
        values : list[int] = [7, 5, 6, 4, 3, 1, 2]
        for kth_order_statistic, _ in enumerate(values):
            pivot_index : int = 4
            new_borders : list[int] = []
            match (kth_order_statistic > pivot_index) - (kth_order_statistic < pivot_index):
                case -1:
                    new_borders = [0, pivot_index - 1]
                    break
                case 0:
                    new_borders = [pivot_index, pivot_index]
                    break
                case 1:
                    new_borders = [pivot_index + 1, len(values) - 1]
                    break
            with self.subTest():
                self.assertEqual(KthOrderStatisticsStep(values.copy(), 0 ,
                    len(values) - 1, kth_order_statistic), new_borders)

unittest.main()
