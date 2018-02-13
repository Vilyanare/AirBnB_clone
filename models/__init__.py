#!/usr/bin/python3
"""Creates a FileStorage instance"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review

classes = {'BaseModel': BaseModel, 'User': User, 'Review': Review,
           'City': City, 'State': State, 'Place': Place, 'Amenity': Amenity}

storage = FileStorage()
storage.reload()
