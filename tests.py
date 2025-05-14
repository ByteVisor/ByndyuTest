import unittest
from typing import Any, List
from main import main  # предполагаем, что основная реализация находится в файле main.py

class TestMainFunction(unittest.TestCase):

    def test_typical_case(self):
        array: List[Any] = [10, 3, 5, 1, 'a', 2]
        self.assertEqual(main(array), 1 + 2)

    def test_only_integers(self):
        array: List[Any] = [9, 5, 8, 2, 3]
        self.assertEqual(main(array), 2 + 3)

    def test_with_floats(self):
        array: List[Any] = [3.5, 1.2, 4.8, 'x', 0.9]
        self.assertAlmostEqual(main(array), 0.9 + 1.2)

    def test_mixed_types(self):
        array: List[Any] = ['hello', 7, 4.5, 'world', -3, 2]
        self.assertEqual(main(array), -3 + 2)

    def test_negative_numbers(self):
        array: List[Any] = [-10, -20, 5, 'a']
        self.assertEqual(main(array), -20 + -10)

    def test_insufficient_numbers(self):
        array: List[Any] = [1]
        with self.assertRaises(ValueError):
            main(array)

    def test_no_numbers(self):
        array: List[Any] = ['a', 'b', 'c']
        with self.assertRaises(ValueError):
            main(array)

    def test_exact_two_numbers(self):
        array: List[Any] = [8, 3]
        self.assertEqual(main(array), 3 + 8)

    def test_duplicates(self):
        array: List[Any] = [1, 1, 2, 3]
        self.assertEqual(main(array), 1 + 1)

if __name__ == "__main__":
    unittest.main()
