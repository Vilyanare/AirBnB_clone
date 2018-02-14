#!/usr/bin/python3
"""Test module for review module"""
import unittest
import models


class TestReview(unittest.TestCase):
    """Class for testing the Review class"""

    def review_is_subclass_base_model(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(models.Review, models.BaseModel))
