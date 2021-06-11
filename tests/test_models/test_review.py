#!/usr/bin/python3
"""Module for TestReview class"""

import unittest
from models.review import Review

review = Review()


class TestReview(unittest.TestCase):
    """Test cases for review.py"""

    def test_place_id(self):
        """Checks that place_id is working correctly"""
        self.assertTrue(type(review.place_id) == str)

    def test_user_id(self):
        """Checks that user_id is working correctly"""
        self.assertTrue(type(review.user_id) == str)

    def test_text(self):
        """Checks that text is working correctly"""
        self.assertTrue(type(review.text) == str)

if __name__ == '__main__':
    unittest.main()
