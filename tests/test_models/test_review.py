#!/usr/bin/python3
"""Test module for review module"""
import unittest
import models


class TestReview(unittest.TestCase):
    """Class for testing the Review class"""

    def setUp(self):
        """Setup for each testcase"""
        self.testcase = models.Review()

    def tearDown(self):
        """Cleanup for every testcase"""
        self.testcase = None

    def test_review_is_subclass_base_model(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(models.Review, models.BaseModel))

    def test_review_place_id(self):
        """Test place_id gets created correctly"""
        self.assertEqual(type(self.testcase.place_id), str)
        self.assertEqual(self.testcase.place_id, "")

    def test_review_user_id(self):
        """Test user_id gets created correctly"""
        self.assertEqual(type(self.testcase.user_id), str)
        self.assertEqual(self.testcase.user_id, "")

    def test_review_text(self):
        """Test text gets created correctly"""
        self.assertEqual(type(self.testcase.text), str)
        self.assertEqual(self.testcase.text, "")
