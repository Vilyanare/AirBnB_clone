#!/usr/bin/python3
"""Test module for user module"""
import unittest
import models


class TestUser(unittest.TestCase):
    """Class for testing the User class"""

    def test_user_is_subclass_base_model(self):
        """Test if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(models.User, models.BaseModel))
