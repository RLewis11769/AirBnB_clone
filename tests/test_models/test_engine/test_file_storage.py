#!/usr/bin/python3

""" Unit tests for file_storage.py """

import unittest
import json
from os import path, remove
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

fs = FileStorage()


class TestFileStorage(unittest.TestCase):
    """ Test cases for file_storage.py """

    def test_filepath(self):
        """ Tests for __file_path existance """
        self.assertTrue(type(fs._FileStorage__file_path) is str)
        tmp = FileStorage()
        try:
            remove("file.json")
        except:
            pass
        tmp.save()
        self.assertTrue(path.exists("file.json"))

    def test_object(self):
        """ Tests for __objects dictionary existance """
        tmp = FileStorage()
        self.assertTrue(type(tmp._FileStorage__objects) is dict)
        self.assertTrue(type(tmp.all()) is dict)

    def test_new(self):
        """ Tests for new method """
        tmp = fs.all().copy()
        BaseModel()
        self.assertFalse(tmp == fs.all())

    def test_save(self):
        """ Tests for save method """
        try:
            remove("file.json")
        except:
            pass
        base = BaseModel()
        base.save()
        with open("file.json") as f:
            tmp = json.load(f)
        self.assertTrue(type(tmp) is dict)

    def test_reload(self):
        """ Tests for reload method """
        fs2 = FileStorage()
        fs2.save()
        fs2.reload()
        tmp = fs2.all()
        BaseModel()
        fs2.save()
        fs2.reload()
        self.assertNotEqual(tmp, fs2.all())

if __name__ == '__main__':
    unittest.main()
