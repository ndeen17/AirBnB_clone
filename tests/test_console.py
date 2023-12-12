#!/usr/bin/python3
"""unittest Test for the console"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """the class test console"""

    def create(self):
        """this create the intance"""
        return HBNBCommand()

    def test_quit(self):
        """this test for the method quit
        """
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """this test for the method EQF
        """
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))
