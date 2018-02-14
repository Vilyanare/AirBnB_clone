#!/usr/bin/python3
"""Test module for city module"""
import unittest
import models


class TestCity(unittest.TestCase):
    """Class for testing the City class"""

    def test_city_is_subclass_base_model(self):
        """Test if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(models.City, models.BaseModel))
