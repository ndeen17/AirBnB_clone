#!/usr/bin/python3
'''the is the class inherent of BaseModel'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''the class Review'''

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """this the initializes Review"""
        super().__init__(*args, **kwargs)

