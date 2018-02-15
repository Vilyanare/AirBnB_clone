#!/usr/bin/python3
"""Test module for user module"""
import unittest
import models


class TestUser(unittest.TestCase):
    """Class for testing the User class"""

    def setUp(self):
        """Setup for each testcase"""
        self.testcase = models.User()

    def tearDown(self):
        """Cleanup for every testcase"""
        self.testcase = None

    def test_user_is_subclass_base_model(self):
        """Test if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(models.User, models.BaseModel))

    def test_user_email(self):
        """Test email gets created correctly"""
        self.assertEqual(type(self.testcase.email), str)
        self.assertEqual(self.testcase.email, "")

    def test_user_password(self):
        """Test password gets created correctly"""
        self.assertEqual(type(self.testcase.password), str)
        self.assertEqual(self.testcase.password, "")

    def test_user_first_name(self):
        """Test first_name gets created correctly"""
        self.assertEqual(type(self.testcase.first_name), str)
        self.assertEqual(self.testcase.first_name, "")

    def test_user_last_name(self):
        """Test last_name gets created correctly"""
        self.assertEqual(type(self.testcase.last_name), str)
        self.assertEqual(self.testcase.last_name, "")
