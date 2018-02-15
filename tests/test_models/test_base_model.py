#!/usr/bin/python3
"""Module to test class BaseModel"""
import models
import unittest
import os
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Class to test BaseModel class with Unittest

    Attributes
    path - json file path
    """

    def setUp(self):
        """Finds json file and renames it so we can make and destroy
        files without deleting data in use"""
        self.path = models.storage._FileStorage__file_path
        if os.path.exists(self.path):
            os.rename(self.path, 'noTouch')
        self.testcase = models.BaseModel()

    def tearDown(self):
        """Renames deletes temp json files and renames old file back
        to original name"""
        if os.path.exists(self.path):
            os.remove(self.path)
        if os.path.exists('noTouch'):
            os.rename('noTouch', self.path)
        self.testcase = None

    def test_id_base_model(self):
        """Test id created correctly and is unique every time"""
        self.assertEqual(len(self.testcase.id), 36)
        self.testcase2 = models.BaseModel()
        self.assertNotEqual(self.testcase.id, self.testcase2.id)
        self.testcase2 = None

    def test_created_at_base_model(self):
        """Test created_at created correctly"""
        self.assertEqual(type(self.testcase.created_at), datetime)

    def test_updated_at_base_model(self):
        """Test updated_at created correctly"""
        self.assertEqual(type(self.testcase.updated_at), datetime)

    def test__str__method_base_model(self):
        """Test __str__ method for correct output"""
        self.assertEqual('[BaseModel]', self.testcase.__str__().split()[0])
        self.assertEqual(38, len(self.testcase.__str__().split()[1]))
        self.assertEqual('{', self.testcase.__str__().split()[2][0])
        self.assertEqual(':', self.testcase.__str__().split()[2][-1])

    def test_save_method_base_model(self):
        """Test save method"""
        first = self.testcase.updated_at
        self.testcase.save()
        self.assertNotEqual(first, self.testcase.updated_at)
        self.assertTrue(os.path.exists(self.path))

    def test_to_dict_method_base_model(self):
        """Test to_dict method"""
        self.assertEqual(type(self.testcase.to_dict()), dict)
        self.assertNotEqual(self.testcase.to_dict().get('id'), None)
        self.assertNotEqual(self.testcase.to_dict().get('created_at'), None)
        self.assertNotEqual(self.testcase.to_dict().get('updated_at'), None)
        self.assertEqual(self.testcase.to_dict().get('__class__'), 'BaseModel')

    def test_kwargs_base_model(self):
        """Test kwargs on init method"""
        testdict = {'created_at': '2018-02-14T04:20:11.699297',
                    'updated_at': '2018-02-14T04:20:11.699315',
                    '__class__': 'BaseModel',
                    'id': '04fac3ec-9ed6-434e-9671-cc47420ebe3d'}
        self.testcase = models.BaseModel(**testdict)
        self.assertEqual(self.testcase.id, '04fac3ec-9ed6-434e-9671-cc47420ebe3d')
        self.assertEqual(type(self.testcase.updated_at), datetime)
        self.assertEqual(type(self.testcase.created_at), datetime)
        self.assertEqual(self.testcase.updated_at.isoformat(),
                         '2018-02-14T04:20:11.699315')
        self.assertEqual(self.testcase.created_at.isoformat(),
                         '2018-02-14T04:20:11.699297')
