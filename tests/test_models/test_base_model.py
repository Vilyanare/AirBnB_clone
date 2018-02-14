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
        path = models.storage._FileStorage__file_path
        if os.path.exists(path):
            os.rename(path, 'noTouch')

    def tearDown(self):
        """Renames deletes temp json files and renames old file back
        to original name"""
        path = models.storage._FileStorage__file_path
        if os.path.exists(path):
            os.remove(path)
        if os.path.exists('noTouch'):
            os.rename('noTouch', path)

    def test_id_base_model(self):
        """Test id created correctly and is unique every time"""
        testcase = models.BaseModel()
        self.assertEqual(len(testcase.id), 36)
        testcase2 = models.BaseModel()
        self.assertNotEqual(testcase.id, testcase2.id)

    def test_created_at_base_model(self):
        """Test created_at created correctly"""
        testcase = models.BaseModel()
        self.assertEqual(type(testcase.created_at), datetime)

    def test_updated_at_base_model(self):
        """Test updated_at created correctly"""
        testcase = models.BaseModel()
        self.assertEqual(type(testcase.updated_at), datetime)

    def test__str__method_base_model(self):
        """Test __str__ method for correct output"""
        testcase = models.BaseModel()
        self.assertEqual('[BaseModel]', testcase.__str__().split()[0])
        self.assertEqual(38, len(testcase.__str__().split()[1]))
        self.assertEqual('{', testcase.__str__().split()[2][0])
        self.assertEqual(':', testcase.__str__().split()[2][-1])

    def test_save_method_base_model(self):
        """Test save method"""
        path = models.storage._FileStorage__file_path
        testcase = models.BaseModel()
        first = testcase.updated_at
        testcase.save()
        self.assertNotEqual(first, testcase.updated_at)
        self.assertTrue(os.path.exists(path))
        os.remove(path)

    def test_to_dict_method_base_model(self):
        """Test to_dict method"""
        testcase = models.BaseModel()
        self.assertEqual(type(testcase.to_dict()), dict)
        self.assertNotEqual(testcase.to_dict().get('id'), None)
        self.assertNotEqual(testcase.to_dict().get('created_at'), None)
        self.assertNotEqual(testcase.to_dict().get('updated_at'), None)
        self.assertEqual(testcase.to_dict().get('__class__'), 'BaseModel')

    def test_kwargs_base_model(self):
        """Test kwargs on init method"""
        testdict = {'created_at': '2018-02-14T04:20:11.699297',
                    'updated_at': '2018-02-14T04:20:11.699315',
                    '__class__': 'BaseModel',
                    'id': '04fac3ec-9ed6-434e-9671-cc47420ebe3d'}
        testcase = models.BaseModel(**testdict)
        self.assertEqual(testcase.id, '04fac3ec-9ed6-434e-9671-cc47420ebe3d')
        self.assertEqual(type(testcase.updated_at), datetime)
        self.assertEqual(type(testcase.created_at), datetime)
        self.assertEqual(testcase.updated_at.isoformat(),
                         '2018-02-14T04:20:11.699315')
        self.assertEqual(testcase.created_at.isoformat(),
                         '2018-02-14T04:20:11.699297')
