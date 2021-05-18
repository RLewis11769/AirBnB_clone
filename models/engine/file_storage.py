#!/usr/bin/python3

""" Module for FileStorage class """


import json
from models.base_model import BaseModel


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
        print(type(FileStorage.__objects))

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
                for key in tmp:
                    if key[:9] == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**tmp[key])
        except:
            pass
