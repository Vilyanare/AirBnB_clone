#!/usr/bin/python3
"""Test module for amenity module"""
import unittest
import models


class TestAmenity(unittest.TestCase):
    """Class for testing the Amenity class"""

    def amenity_is_subclass_base_model(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(models.Amenity, models.BaseModel))
