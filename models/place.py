#!/usr/bin/python3
"""Module holding the Place class"""
import models


class Place(models.BaseModel):
    """
    Class holding information building details

    Attributes
    city_id - id of city place is located
    state_id - id of state place is located
    name - name of place
    description - description of place
    number_rooms - number of rooms
    number_bathrooms - number of bathrooms
    max_guest - max amount of guests allowed
    price_by_night - how much it costs per night to stay
    latitude - latitude of place
    longitude - longitude of place
    amenity_ids - list of amenities by id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
