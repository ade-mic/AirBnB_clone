#!/usr/bin/python3
"""
This module contain a a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances
"""
import json
import os

class FileStorage:
    """
    This class class serializes instances to a JSON file
    and desirializr JSON file to instances
    Private class attributes:
        __file_path (string):
            path to the JSON file (ex: file.json)
        __objects (dictionary)
         empty but will store all objects by
         <class name>.id (ex:
         to store a BaseModel object with id=12121212,
         the key will be BaseModel.12121212)
    Public instance methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
    """

    def __init__(self):
        file_path = 'file.json'
        # private class attribute
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """
        Returns the dictionary objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with
        key <obj class name>.id
        """
        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to the JSON file path
        path = _file_path
        """
        serializable_objs = {}
        for key, obj in self.__objects.items():
            if hasattr(obj, 'to_dict') and callable(getattr(obj, 'to_dict')):
                serializable_objs[key] = obj.to_dict()
            else:
                serializable_objs[key] = obj
        with open(self.__file_path, "w") as f:
            json.dump(serializable_objs, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        # check if file
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id  = key.split(".")
                    from models.base_model import BaseModel
                    from models.user import User
                    from models.place import Place
                    from models.state import State
                    from models.city import City
                    from models.amenity import Amenity
                    from models.review import Review
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
                    elif class_name == "User":
                        self.__objects[key] = User(**value)
                    elif class_name == "Place":
                        self.__objects[key] = Place(**value)
                    elif class_name == "State":
                        self.__objects[key] = State(**value)
                    elif class_name == "City":
                        self.objects[key] = City(**value)
                    elif class_name == "Review":
                        self.objects[key] = Review(**value)
        except FileNotFoundError:
            pass
