#!/usr/bin/python3
"""Module for TestUser class"""

import unittest
from models.user import User

usr = User()


class TestUser(unittest.TestCase):
    """Test cases for user.py"""

    def test_email(self):
        """Checks that email is working correctly"""
        self.assertTrue(type(usr.email) == str)

    def test_password(self):
        """Checks that password is working correctly"""
        self.assertTrue(type(usr.password) == str)

    def test_first_name(self):
        """Checks that first_name is working correctly"""
        self.assertTrue(type(usr.first_name) == str)

    def test_last_name(self):
        """Checks that last_name is working correctly"""
        self.assertTrue(type(usr.last_name) == str)

if __name__ == '__main__':
    unittest.main()
