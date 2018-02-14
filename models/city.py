#!/usr/bin/python3
"""Module holding the City class"""
import models


class City(models.BaseModel):
    """
    Class that holds city information

    Attributes
    state_id - id of the state the city is in
    name - name of the city
    """

    state_id = ""
    name = ""
