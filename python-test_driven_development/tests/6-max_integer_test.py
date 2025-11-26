#!/usr/bin/python3
"""Unittest for max_integer()"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function"""

    def test_ordered_list(self):
        """Max of an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max of an unordered list"""
        self.assertEqual(max_integer([2, 4, 1, 3]), 4)

    def test_max_at_beginning(self):
        """Max at the beginning"""
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)

    def test_single_element(self):
        """List with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Call without argument uses default list and returns None"""
        self.assertIsNone(max_integer())

    def test_all_negative(self):
        """All negative numbers"""
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_positive_negative(self):
        """Mixed positive and negative numbers"""
        self.assertEqual(max_integer([-3, -1, 0, 2, -10]), 2)

    def test_all_equal(self):
        """All elements equal"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_float_list(self):
        """List of floats"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_string_list(self):
        """List of strings (lexicographical max)"""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_mixed_types_in_list(self):
        """List with mixed incompatible types raises TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])

    def test_non_iterable_argument(self):
        """Passing non-iterable (like int or None) raises TypeError"""
        with self.assertRaises(TypeError):
            max_integer(4)
        with self.assertRaises(TypeError):
            max_integer(None)
