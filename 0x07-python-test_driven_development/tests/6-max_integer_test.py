#!/usr/bin/python3
"""Unit test for 6-max_integer_test.py"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_module_docstring(self):
        """Tests for module docstring"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Tests fo function docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_one_element(self):
        """Only one number in list"""
        only_one = [7]
        self.assertEqual(max_integer(only_one), 7)

    def test_floats(self):
        '''Test for floats'''
        flts = [5.7, 3.8, 9.7, 2.1]
        self.assertEqual(max_integer(flts), 9.7)

    def test_int_n_floats(self):
        '''Test for ints and floats'''
        ints_n_floats = [4, 6.7, 4, 10]
        self.assertEqual(max_integer(ints_n_floats), 10)

    def test_ints(self):
        '''unordered ints'''
        u_ints = [5, 2, 7, 3, 8]
        self.assertEqual(max_integer(u_ints), 8)

    def test_string(self):
        '''Test a string'''
        str = "Bencity"
        self.assertEqual(max_integer(str), 'y')

    def test_list_of_strings(self):
        '''Test a list of strings'''
        str = ["Winter", "is", "coming"]
        self.assertEqual(max_integer(str), "name")

    def test_empty_string(self):
        '''Test an empty string'''
        str = []
        self.assertEqual(max_integer(str), None)


if __name__ == '__main__':
    unittest.main()

