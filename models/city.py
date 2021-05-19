#!/usr/bin/python3
"""Module for City class"""

import models.base_model import BaseModel


class City(BaseModel):
    """Subclass of BaseModel with class attributes state_id and name"""
    state_id = ""
    name = ""
