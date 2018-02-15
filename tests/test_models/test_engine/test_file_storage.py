#!/usr/bin/python3
""" Unittest for FileStorage class
"""
import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Utilizes unittest to evaluate possible outcomes of
    creating instances of FileStorage class
    """

    def setUp(self):
        """sets up testing environment so previous file storage
        is not affected"""
        file_path = models.storage._FileStorage__file_path
        self.my_path = models.storage._FileStorage__file_path
        if os.path.exists(file_path):
            os.rename(file_path, 'test_storage')
        self.testcase = FileStorage()

    def tearDown(self):
        """ Removes JSON file after test cases run """
        file_path = models.storage._FileStorage__file_path
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists('test_storage'):
            os.rename('test_storage', file_path)
        self.testcase = None

    def test_save_1(self):
        """testing if save saves new instance properly
        """
        my_model = BaseModel()
        my_storage = FileStorage()
        my_storage.new(my_model)
        my_storage.save()
        file_existence = os.path.exists(self.my_path)
        self.assertEqual(True, file_existence)

    def test_save_2(self):
        """tests if updating attributes saves properly"""
        my_model = BaseModel()
        my_storage = FileStorage()
        my_model.my_number = 89
        my_storage.save()
        self.assertEqual(my_model.my_number, 89)

    def test_save_3(self):
        """tests if file contains correct id after saving"""
        my_model = BaseModel()
        my_storage = FileStorage()
        my_storage.save()
        desired_str = 'BaseModel.' + my_model.id
        with open(self.my_path, "r", encoding="utf-8") as f:
            if desired_str in f.read():
                result = True
            else:
                result = False
        self.assertEqual(result, True)

    def test_file_path(self):
        """testing if file saves as correct file path name"""
        my_storage = FileStorage()
        my_storage.save()
        expected_name = self.my_path
        self.assertEqual(expected_name, my_storage._FileStorage__file_path)

    def test_file_empty(self):
        """testing if file saves properly, and doesn't return an
        empty file"""
        my_model = BaseModel()
        my_storage = FileStorage()
        my_storage.new(my_model)
        my_storage.save()
        self.assertEqual(os.stat(self.my_path).st_size == 0, False)

    def test_file_storage_file_path_exists(self):
        """Tests if __file_path is created correctly"""
        self.assertEqual(type(self.testcase._FileStorage__file_path), str)

    def test_file_storage_objects_exists(self):
        """Test if __objects is created correctly"""
        self.assertEqual(type(self.testcase._FileStorage__objects), dict)

    def test_file_storage_all_method(self):
        """Test all method"""
        my_model = BaseModel()
        my_storage = FileStorage()
        my_dict = my_storage.all()
        self.assertEqual(my_dict, my_storage._FileStorage__objects)


    def test_file_storage_new_method(self):
        """Test new method"""
        my_model = BaseModel()
        my_storage = FileStorage()
        my_storage.new(my_model)
        my_storage.save()
        desired_key = my_model.__class__.__name__ + '.' + my_model.id
        for key in my_storage._FileStorage__objects:
            if key == desired_key:
                self.assertEqual(desired_key, key)
