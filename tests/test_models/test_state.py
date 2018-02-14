#!/usr/bin/python3
"""Test module for state module"""
import unittest
import models


class TestState(unittest.TestCase):
    """Class for testing the State class"""

    def state_is_subclass_base_model(self):
        """Test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(models.State, models.BaseModel))
