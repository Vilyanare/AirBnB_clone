#!/usr/bin/python3
"""Test module for city module"""
import unittest
import models


class TestCity(unittest.TestCase):
    """Class for testing the City class"""

    def setUp(self):
        """Setup for each testcase"""
        self.testcase = models.City()

    def tearDown(self):
        """Cleanup for every testcase"""
        self.testcase = None

    def test_city_is_subclass_base_model(self):
        """Test if city is a subclass of BaseModel"""
        self.assertTrue(issubclass(models.City, models.BaseModel))

    def test_city_name(self):
        """Test name gets created correctly"""
        self.assertEqual(type(self.testcase.name), str)
        self.assertEqual(self.testcase.name, "")

    def test_city_state_id(self):
        """Test name gets created correctly"""
        self.assertEqual(type(self.testcase.state_id), str)
        self.assertEqual(self.testcase.state_id, "")
