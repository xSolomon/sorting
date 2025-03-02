''' Tests for lesson 11 solution. '''

import unittest
from sorting11_1 import BinarySearch

class BinarySearchTests(unittest.TestCase):
    ''' Tests for BinarySearch class. '''
    def prepare_binary_search_on(self, values_ascending : list[int]) -> BinarySearch:
        ''' Creates new BinarySearch instance on provided ary and returns it. '''
        return BinarySearch(values_ascending)

    def test_creating_binary_seach(self) -> None:
        ''' Creates BinarySearch instances on different arys.
            Expected correct initializing of public fields. '''
        sorted_arrays : list[list[int]] = [
            [],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [1],
            [1, 2, 3, 4, 5],
            [1, 2],
            [1, 2, 3],
            [x for x in range(10000)]
        ]
        for array in sorted_arrays:
            search : BinarySearch = self.prepare_binary_search_on(array)
            with self.subTest():
                self.assertEqual(search.Left, 0)
                self.assertEqual(search.Right, len(array) - 1)

    def test_get_result_before_steps(self) -> None:
        ''' Cause no steps made, search status = 0. '''
        sorted_arrays : list[list[int]] = [
            [],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [1],
            [1, 2, 3, 4, 5],
            [1, 2],
            [1, 2, 3],
            [x for x in range(10000)]
        ]
        for array in sorted_arrays:
            search : BinarySearch = self.prepare_binary_search_on(array)
            with self.subTest():
                self.assertEqual(search.GetResult(), 0)

    def test_step_on_empty_ary(self) -> None:
        ''' After first step, search status must be -1.
            Next steps should do nothing. '''
        search : BinarySearch = self.prepare_binary_search_on([])
        search.Step(5)
        self.assertEqual(search.GetResult(), -1)
        self.assertEqual(search.Left, 0)
        self.assertEqual(search.Right, -1)
        search.Step(5)
        self.assertEqual(search.GetResult(), -1)
        self.assertEqual(search.Left, 0)
        self.assertEqual(search.Right, -1)

    def test_step_on_one_element_ary(self) -> None:
        ''' If key exists, result must be 1 after 1 step.
            Result must be -1 after 1 step otherwise.
            Steps past first should do nothing. '''
        search : BinarySearch = self.prepare_binary_search_on([5])
        with self.subTest():
            search.Step(5)
            self.assertEqual(search.GetResult(), 1)
            self.assertEqual(search.Left, 0)
            self.assertEqual(search.Right, 0)
            search.Step(5)
            self.assertEqual(search.GetResult(), 1)
            self.assertEqual(search.Left, 0)
            self.assertEqual(search.Right, 0)
        search = self.prepare_binary_search_on([5])
        with self.subTest():
            search.Step(3)
            self.assertEqual(search.GetResult(), -1)
            self.assertEqual(search.Left, 0)
            self.assertEqual(search.Right, -1)
            search.Step(3)
            self.assertEqual(search.GetResult(), -1)
            self.assertEqual(search.Left, 0)
            self.assertEqual(search.Right, -1)

    def test_search_on_five_element_ary(self) -> None:
        ''' Each number should take expected number of steps. '''
        values : list[int] = [1, 2, 3, 4, 5]
        steps_number : list[int] = [2, 2, 3, 1, 2, 3, 3]
        final_status : list[int] = [-1, 1, 1, 1, 1, 1, -1]
        for i in range(0, 7):
            value_for_search : int = i
            binary_searh : BinarySearch = self.prepare_binary_search_on(values)
            with self.subTest(value = value_for_search):
                for _ in range(steps_number[i] - 1):
                    binary_searh.Step(value_for_search)
                    self.assertEqual(binary_searh.GetResult(), 0)
                binary_searh.Step(value_for_search)
                self.assertEqual(binary_searh.GetResult(), final_status[i])

unittest.main()
