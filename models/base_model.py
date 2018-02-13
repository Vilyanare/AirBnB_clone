#!/usr/bin/python3
"""Module containing the BaseModel class"""
import uuid
from datetime import datetime
import models
from copy import deepcopy


class BaseModel:
    """
    Class to setup all future classes in AirBnB_clone project

    Attributes:
    id - unique id for all instances of a class
    created_at - time instance was created
    updated_at - time instance was updated
    """
    def __init__(self, *args, **kwargs):
        """initializeing method of BaseModel class"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k in ("created_at", "updated_at"):
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)

    def __str__(self):
        """returns a informal representation of BaseModel instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def __repr__(self):
        """returns a informal representation of BaseModel instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the attribute updated_at
        with current datettime and save to file"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all attributes from __dict__,
        a __class__ attribute holding the name of the class and
        updated_at and created_at are now strings"""
        new = deepcopy(self.__dict__)
        new['__class__'] = self.__class__.__name__
        new['updated_at'] = self.updated_at.isoformat()
        new['created_at'] = self.created_at.isoformat()
        return new
