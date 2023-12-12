#!/usr/bin/python3
'''this is a class user that inherent from BaseModel'''
from models.base_model import BaseModel


class User(BaseModel):
    '''this represent a class User'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

