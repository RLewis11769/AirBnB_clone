#!/usr/bin/python3
"""Module for user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """subclass of BaseModel with class attributes: email, password,
    first_name, and last_name"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
