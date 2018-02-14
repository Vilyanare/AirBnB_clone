#!/usr/bin/python3
"""Module to test class BaseModel"""
import models
import unittest


class TestBaseModel(unittest):
    """Class to test BaseModel class with Unittest"""
    def test_id(self):
        """Test id created correctly and is unique every time"""
        testcase = models.BaseModel()
        self.assertEqual(len(testcase.id), 36)
        testcase2 = models.BaseModel()
        self.assertNotEqual(testcase.id, testcase2.id)

    def test_created_at(self):
       """Test created_at created correctly"""
       testcase = models.BaseModel()
       self.assert

    def test_updated_at(self)
        """Test updated_at created correctly"""
    def test__str__method(self):
       """Test __str__ method for correct output"""

    def test_save_method(self):
        """Test save method"""

    def test_to_dict_method(self):
        """Test to_dict method"""

    def test_kwargs(self):
        """Test kwargs on init method"""
