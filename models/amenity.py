#!/usr/bin/python3
'''the class inherent of BaseModel'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''the class amenity'''

    name = ""

    def __init__(self, *args, **kwargs):
        """this initializes the Amenity"""
        super().__init__(*args, **kwargs)

