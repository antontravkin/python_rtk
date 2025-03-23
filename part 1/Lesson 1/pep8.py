"""PEP8"""

from hmac import new
import os
from random import randint
import sys


class Application(object):
    """Test class"""

    def __init__(self,app_id=None):
        self.app_id = app_id
        self.app_id = "Test application"


    def rename(self, new_name):
        self.name = new_name
        print("New name: " + new_name)


    def random_id(self):
        print(randint(1, 999999))
        
