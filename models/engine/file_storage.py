#!/usr/bin/python3

""" Module for FileStorage class """


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
           'Amenity': Amenity, 'Place': Place, 'Review': Review}


class FileStorage():
    """ Methods and attributes for FileStorage class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns dictionary objects """
        return FileStorage.__objects

    def new(self, obj):
        """Sets obj with key <class_name>.id """
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ Serializes __objects dictionary to json file """
        with open(FileStorage.__file_path, 'w') as f:
            tmp = {}
            for key in FileStorage.__objects.keys():
                tmp[key] = FileStorage.__objects[key].to_dict()
            json.dump(tmp, f)

    def reload(self):
        """ Deserializes json file to __objects dictionary """
        try:
            with open(FileStorage.__file_path) as f:
                FileStorage.__objects = {}
                tmp = json.load(f)
                for key, val in tmp.items():
                    for k, v in classes.items():
                        if key.split('.')[0] == k:
                            FileStorage.__objects[key] = v(**val)
        except:
            pass
