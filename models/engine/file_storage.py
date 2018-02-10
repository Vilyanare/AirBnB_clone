#!/usr/bin/python3
"""Module holding FilesStorage class"""
import json

class FileStorage:
    """
    Handles serialization and deserialization of JSON files to instances

    Attributes
    __file_path - path to JSON file
    __objects - Dictionary of dictionary objects
    """

    def __init__(self):
        """initialises FileStorage class instances"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """Sets key/value pair in __object dictionary"""
        self.__objects['{}.{}'.format(obj.__class__.__name__, obj.id)] = obj.to_dict()

    def save(self):
        """serealizes __objects to JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserealizes JSON file into __objects"""
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
