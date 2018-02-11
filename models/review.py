#!/usr/bin/python3
"""Module holding the class Review"""
import models

class Review(models.BaseModel):
    """
    Class holding reviews for places

    Attributes
    place_id - id of the place being reviewed
    user_id - user who left review
    text - the review
    """
    place_id = ""
    user_id = ""
    text = ""
