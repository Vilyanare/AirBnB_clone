#!/usr/bin/python3
"""Test module for state module"""
import unittest
import models


class TestState(unittest.TestCase):
    """Class for testing the State class"""

    def setUp(self):
        """Setup for each testcase"""
        self.testcase = models.State()

    def tearDown(self):
        """Cleanup for every testcase"""
        self.testcase = None

    def test_state_is_subclass_base_model(self):
        """Test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(models.State, models.BaseModel))

    def test_state_name(self):
        """Test name gets created correctly"""
        self.assertEqual(type(self.testcase.name), str)
        self.assertEqual(self.testcase.name, "")
