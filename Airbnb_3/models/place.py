#!/usr/bin/python3
"""
In this module the class Place which inherits from the class BaseModel
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """ Initialization of the class attributes """

    city_id = "" #will be the City.id
    user_id = "" # will be the User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [] # will be the list of Amenity.id later
