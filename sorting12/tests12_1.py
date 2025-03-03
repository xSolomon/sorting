''' Tests for lesson 12 solution. '''

import unittest
from sorting12_1 import GallopingSearch

class GallopingSearchTests(unittest.TestCase):
    ''' Tests for GallopingSearch function of BinarySearch class. '''

    def test_on_empty_ary(self) -> None:
        ''' Must return false. '''
        self.assertFalse(GallopingSearch([], 0))

    def test_on_one_element_ary(self) -> None:
        ''' Expected true when searching for this single element.
            false otherwise. '''
        values_to_search : list[int] = [-5, -1, 0, 1, 2, 3, 4, 5]
        ary : list[int] = [3]
        for search_value in values_to_search:
            expected_result : bool = ary[0] == search_value
            with self.subTest(search_value = search_value):
                self.assertEqual(GallopingSearch(ary, search_value),
                    expected_result)

    def test_on_seven_element_ary(self) -> None:
        ''' Expected true when key exists, false otherwise. '''
        values_to_search : list[int] = [-341414, 463663, -5, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ary : list[int] = [1, 2, 3, 4, 5, 6, 7]
        for search_value in values_to_search:
            expected_result : bool = search_value in ary
            with self.subTest(search_value = search_value):
                self.assertEqual(GallopingSearch(ary, search_value),
                    expected_result)

unittest.main()
