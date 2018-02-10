#!/usr/bin/python3
"""Module that holds the class User"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    Class to keep track of users

    Attributes
    email - Email address of user
    password - Password for user
    first_name - First name of user
    last_name - Last name of user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
