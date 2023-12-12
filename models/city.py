#!/usr/bin/python3
'''this is the class inherent of BaseModel'''
from models.base_model import BaseModel


class City(BaseModel):
    '''the class city'''

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """this is the initializes City"""
        super().__init__(*args, **kwargs)
