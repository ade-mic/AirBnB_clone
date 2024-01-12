#!/usr/bin/python3
"""
a class Amenity  that inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    a class Amenity that inherits from BaseModel
    Public class attributes:
        name: string - empty string
    """
    state = ""

    def __init__(self, **kwargs):
        """
        Class Constructor
        """
        super().__init__(self, **kwargs)
