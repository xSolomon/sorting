''' Tests for lesson 10 solution. '''

import unittest
from sorting10_1 import ksort

letters : list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
digits : list[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

correct_strings : list[str] = []
for first_symbol in letters:
    for second_symbol in digits:
        for third_symbol in digits:
            correct_strings.append(first_symbol + second_symbol + third_symbol)

class KsortTests(unittest.TestCase):
    ''' Tests correct class creation. '''
    def test_creating_ksort(self) -> None:
        ''' Expected correct length. '''
        ksort_object : ksort = ksort()
        self.assertEqual(len(ksort_object.items), len(correct_strings))

class IndexTests(unittest.TestCase):
    ''' Tests for index method. '''
    def setUp(self) -> None:
        ''' Tests preparations. '''
        self.ksort = ksort()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.ksort = None

    def test_on_incorrect_strings(self) -> None:
        ''' Expected -1 for each string. '''
        strings : list[str] = [
            '',
            'a',
            '0',
            '+'
            '111',
            'aaa',
            '+++',
            'a0a',
            'z11',
            '+11',
            'a+1',
            'a1+',
            '1234',
            'a123',
            'a12a',
            '1a11',
            '414141414',
            'afafafafaf',
            'i00',
            'i99'
        ]
        for string in strings:
            with self.subTest(string = string):
                self.assertEqual(self.ksort.index(string), -1)

    def test_on_correct_strings(self) -> None:
        ''' For each string, expected correct index. '''
        for expected_index, correct_string in enumerate(correct_strings):
            with self.subTest(string = correct_string, expected_index = expected_index):
                self.assertEqual(self.ksort.index(correct_string), expected_index)

class AddTests(unittest.TestCase):
    ''' Tests for add function. '''
    def setUp(self) -> None:
        ''' Tests preparations. '''
        self.ksort = ksort()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.ksort = None

    def test_on_incorrect_strings(self) -> None:
        ''' Expected false for each string. '''
        strings : list[str] = [
            '',
            'a',
            '0',
            '+'
            '111',
            'aaa',
            '+++',
            'a0a',
            'z11',
            '+11',
            'a+1',
            'a1+',
            '1234',
            'a123',
            'a12a',
            '1a11',
            '414141414',
            'afafafafaf',
            'i00',
            'i99'
        ]
        for string in strings:
            with self.subTest(string = string):
                self.assertFalse(self.ksort.add(string))

    def test_on_correct_strings(self) -> None:
        ''' For each string, expected true for adding.
            Index of added string must be correct. '''
        for expected_index, correct_string in enumerate(correct_strings):
            with self.subTest(string = correct_string, expected_index = expected_index):
                self.assertTrue(self.ksort.add(correct_string))
                self.assertEqual(self.ksort.items[self.ksort.index(correct_string)], correct_string)

unittest.main()
