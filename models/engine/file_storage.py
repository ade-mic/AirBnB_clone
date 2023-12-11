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
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

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
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                self.__objects = data
