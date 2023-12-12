#!/usr/bin/python3
"""this create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage

"""this is A variable storage, an instance of FileStorage"""
storage = FileStorage()
storage.reload()
