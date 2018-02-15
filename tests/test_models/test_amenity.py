#!/usr/bin/python3
"""Test module for amenity module"""
import unittest
import models


class TestAmenity(unittest.TestCase):
    """Class for testing the Amenity class"""

    def setUp(self):
        """Setup for each testcase"""
        self.testcase = models.Amenity()

    def tearDown(self):
        """Cleanup for every testcase"""
        self.testcase = None

    def test_amenity_is_subclass_base_model(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(models.Amenity, models.BaseModel))

    def test_amenity_name(self):
        """Test name gets created correctly"""
        self.assertEqual(type(self.testcase.name), str)
        self.assertEqual(self.testcase.name, "")
