#!/usr/bin/python3

""" Module for BaseModel class """

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Methods and attributes of BaseModel class """

    def __init__(self, *args, **kwargs):
        """ Instantiates attributes """
        if kwargs and len(kwargs):
            for key in kwargs.keys():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.
                                strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns string representation of instance """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Updates updated_at when saved """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Creates dictionary in json format of attributes """
        new_dict = {}
        for key in self.__dict__:
            if key == "created_at" or key == "updated_at":
                value = self.__dict__[key].isoformat()
            else:
                value = self.__dict__[key]
            new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
