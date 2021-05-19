#!/usr/bin/python3
"""Module for Review class"""

import models.base_model import BaseModel


class Review(BaseModel):
    """Subclass of BaseModel with class attributes: place_id, user_id,
    and text"""
    place_id = ""
    user_id = ""
    text = ""
