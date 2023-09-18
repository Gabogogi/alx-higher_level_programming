#!/usr/bin/python3
'''tests for base.py'''


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    '''unit test for instantiation'''

    def test_no_args_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_isNone(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(4, Base(4).id)
    
    def test_nb_between(self):
        b1 = Base()
        b2 = Base(7)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)
    
    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(5).__nb_instances)

    def test_str_id(self):
        b = Base("Five")
        self.assertEqual("Five", b.id)
    
    def test_float_id(self):
        self.assertEqual(8.5, Base(8.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(7), Base(complex(7)).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([9, 8, 7], Base([9, 8, 7]).id)

    def test_tuple_id(self):
        self.assertEqual((4, 7), Base((4, 7)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_inf(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)
    
