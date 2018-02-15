#!/usr/bin/python3
"""Test module for place module"""
import unittest
import models


class TestPlace(unittest.TestCase):
    """Class for testing the Place class"""

    def setUp(self):
        """Setup for each testcase"""
        self.testcase = models.Place()

    def tearDown(self):
        """Cleanup for every testcase"""
        self.testcase = None

    def test_place_is_subclass_base_model(self):
        """Test if Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(models.Place, models.BaseModel))

    def test_place_name(self):
        """Test name gets created correctly"""
        self.assertEqual(type(self.testcase.name), str)
        self.assertEqual(self.testcase.name, "")

    def test_place_city_id(self):
        """Test city_id gets created correctly"""
        self.assertEqual(type(self.testcase.city_id), str)
        self.assertEqual(self.testcase.city_id, "")

    def test_place_user_id(self):
        """Test user_id gets created correctly"""
        self.assertEqual(type(self.testcase.user_id), str)
        self.assertEqual(self.testcase.user_id, "")

    def test_place_description(self):
        """Test description gets created correctly"""
        self.assertEqual(type(self.testcase.description), str)
        self.assertEqual(self.testcase.description, "")

    def test_place_number_rooms(self):
        """Test number_rooms gets created correctly"""
        self.assertEqual(type(self.testcase.number_rooms), int)
        self.assertEqual(self.testcase.number_rooms, 0)

    def test_place_number_bathrooms(self):
        """Test number_bathrooms gets created correctly"""
        self.assertEqual(type(self.testcase.number_bathrooms), int)
        self.assertEqual(self.testcase.number_bathrooms, 0)

    def test_place_max_guest(self):
        """Test max_guest gets created correctly"""
        self.assertEqual(type(self.testcase.max_guest), int)
        self.assertEqual(self.testcase.max_guest, 0)

    def test_place_price_by_night(self):
        """Test price_by_night gets created correctly"""
        self.assertEqual(type(self.testcase.price_by_night), int)
        self.assertEqual(self.testcase.price_by_night, 0)

    def test_place_latitude(self):
        """Test latitude gets created correctly"""
        self.assertEqual(type(self.testcase.latitude), float)
        self.assertEqual(self.testcase.latitude, 0.0)

    def test_place_longitude(self):
        """Test longitude gets created correctly"""
        self.assertEqual(type(self.testcase.longitude), float)
        self.assertEqual(self.testcase.longitude, 0.0)

    def test_place_amenity_ids(self):
        """Test amenity_ids gets created correctly"""
        self.assertEqual(type(self.testcase.amenity_ids), list)
        self.assertEqual(self.testcase.amenity_ids, [])
