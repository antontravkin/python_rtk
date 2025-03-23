"""PEP8"""


import os
import sys

from random import randint
from hmac import new


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
        
