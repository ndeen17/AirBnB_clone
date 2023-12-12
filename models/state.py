#!/usr/bin/python3
'''this is the class inherent of BaseModel'''
from models.base_model import BaseModel


class State(BaseModel):
    '''the class State'''

    name = ""

    def __init__(self, *args, **kwargs):
        """this initializes State"""
        super().__init__(*args, **kwargs)

