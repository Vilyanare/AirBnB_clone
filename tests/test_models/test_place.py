#!/usr/bin/python3
"""Test module for place module"""
import unittest
import models


class TestPlace(unittest.TestCase):
    """Class for testing the Place class"""

    def place_is_subclass_base_model(self):
        """Test if Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(models.Place, models.BaseModel))
