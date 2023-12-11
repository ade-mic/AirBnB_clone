#!/usr/bin/python3
"""
The files consist a class BaseModel that defines all common
attributes/methods for other classes
"""
import uuid
import datetime
from models import storage


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    Public instance attributes:
        id: string - assign with an uuid when an instance is created:
        created_at: datetime - assign with the current datetime
        when an instance is created
        updated_at: datetime - assign with the current datetime
        when an instance is created
        and it will be updated every time you change your object
    Public instance methods:
        save(self): updates the public instance attribute
        updated_at with the current datetime
        to_dict(self): returns a dictionary containing all
        keys/values of __dict__ of the instance:
        by using self.__dict__, only instance attributes set will be returned
        a key __class__ must be added to this dictionary with
        the class name of the object
        created_at and updated_at must be converted to string object
        in ISO format:
        format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
    """
    def __init__(self, *args, **kwargs):
        """
        Object Constructor: Creates an instance of the BaseModel
        """
        # check if kwargs
        if kwargs:
            for key, item in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        self.__dict__[key] = datetime.datetime.strptime(
                            item, "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = item
        else:
            # Randomly generate id and then convert to string
            self.id = str(uuid.uuid4())
            # Assign the time when an instance was
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """ String representation of an object"""
        return '[{}] ({}) {}'.format(type(self).__name__,
                                       self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_atwith
          the current datetime
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
         returns a dictionary containing all keys/values
           of __dict__ of the instance
        """
        # create a copy of the __dict__ attr
        dictionary = self.__dict__.copy()
        # add the __class__ key wiith the class name value
        dictionary['__class__'] = type(self).__name__
        # convert created_at and updated_at to string using ISO format
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
