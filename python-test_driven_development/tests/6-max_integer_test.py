#!/usr/bin/python3
"""This module contains unit-tests for function max_integer"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_intger(self):
        """
        test_max_intger - tests max_integer function
        Args:
            Nothing
        Return:
            Nothing
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1, -10, -9, -2]), -1)
        self.assertEqual(max_integer([100, 1, 0, -1]), 100)
        self.assertEqual(max_integer([0, 10, 1]), 10)
        #  self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        #  self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        #  self.assertEqual(max_integer([1, 1.5, 0.6, 0]), 1.5)
        #  self.assertEqual(max_integer((2, 4, 10, 5)), 10)
        #  self.assertRaises(TypeError, max_integer(["Magomed", "Abil", "Bilandar"]))
        #  self.assertRaises(TypeError, max_integer([[1, 2, 4], [1, 4], [4, 2, 1]]))
        #  self.assertRaises(TypeError, max_integer(10))
        #  self.assertRaises(TypeError, max_integer("Hello world"))
        #  self.assertRaises(TypeError, max_integer([1, 4, 2, "1"]))
