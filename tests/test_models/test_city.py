#!/usr/bin/python3
"""Module for TestCity class"""

import unittest
from models.city import City

city = City()


class TestCity(unittest.TestCase):
    """Test cases for city.py"""

    def test_state_id(self):
        """Checks that state_id is working correctly"""
        self.assertTrue(type(city.state_id) == str)

    def test_name(self):
        """Checks that name is working correctly"""
        self.assertTrue(type(city.name) == str)

if __name__ == '__main__':
    unittest.main()
