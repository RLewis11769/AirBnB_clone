#!/usr/bin/python3
"""Module for TestState class"""

import unittest
from models.state import State

state = State()


class TestState(unittest.TestCase):
    """Test cases for state.py"""

    def test_name(self):
        """Checks that name is working correctly"""
        self.assertTrue(type(state.name) == str)

if __name__ == '__main__':
    unittest.main()
