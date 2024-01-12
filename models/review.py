#!/usr/bin/python3
"""
a class Review  that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    a class Review that inherits from BaseModel
    Public class attributes:
       place_id: string - empty string: it will be the Place.id
       user_id: string - empty string: it will be the User.id
       text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, **kwargs):
        """
        Class Constructor
        """
        super().__init__(self, **kwargs)
