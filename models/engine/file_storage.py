#!/usr/bin/python3
"""Module holding FilesStorage class"""
import json
import models

class FileStorage:
    """
    Handles serialization and deserialization of JSON files to instances

    Attributes
    __file_path - path to JSON file
    __objects - Dictionary of class instance objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns __objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Puts a new object into __object dictionary"""
        FileStorage.__objects['{}.{}'.format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serealizes __objects to JSON file"""
        tmpobjdict = {}
        for k, v in FileStorage.__objects.items():
            tmpobjdict[k] = v.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(tmpobjdict, f)

    def reload(self):
        """deserealizes JSON file into __objects"""
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                tempobjdict = json.load(f)
            for k, v in tempobjdict.items():
                FileStorage.__objects[k] = models.classes[tempobjdict[k]['__class__']](**v)
        except FileNotFoundError:
            pass
