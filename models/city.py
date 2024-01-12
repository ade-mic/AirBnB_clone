#!/usr/bin/python3
"""
a class City  that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    a class City that inherits from BaseModel
    Public class attributes:
        name: string - empty string
        state.id: string - empty it will be the State.id

    """
    state_id = ""
    name = ""

    def __init__(self, **kwargs):
        """
        Class Constructor
        """
        super().__init__(self, **kwargs)
