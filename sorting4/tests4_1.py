''' Tests for lesson 4 solution. '''

import unittest
from typing import Tuple
from sorting4_1 import ArrayChunk

class ArrayChunkTests(unittest.TestCase):
    ''' Tests for ArrayChunk function. '''
    def test_on_empty_array(self) -> None:
        ''' Expected None as pivot, array shouldn't change. '''
        values : list[int] = []
        self.assertIsNone(ArrayChunk(values))
        self.assertEqual(values, [])

    def test_on_seven_elements_array(self) -> None:
        ''' Expected correct pivot and changes to array. '''
        values : list[int] = [7, 5, 6, 4, 3, 1, 2]
        results : Tuple[int, list[int]] = (3, [2, 1, 3, 4, 6, 5, 7])
        self.assertEqual(ArrayChunk(values), results[0])
        self.assertEqual(values, results[1])

unittest.main()
