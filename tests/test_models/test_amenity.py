#!/usr/bin/python3
"""Module for TestAmenity class"""

import unittest
from models.amenity import Amenity

amenity = Amenity()


class TestAmenity(unittest.TestCase):
    """Test cases for amenity.py"""

    def test_name(self):
        """Checks that name is working correctly"""
        self.assertTrue(type(amenity.name) == str)

if __name__ == '__main__':
    unittest.main()
