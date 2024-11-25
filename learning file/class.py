# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:25:35 2020

@author: User
"""

class Dog:
    """a simple attempt to model a Dog"""
    
    def __init__(self,name,age):
        """initialize name and age atrributes."""
        self.name=name
        self.age=age
        
    def sit(self):
        """simulate a dog sitting inresponse to a command"""
        print(f"{self.name} is now sitting.")
        
    def roll_ove(self):
        """simulatr rolling over in response to a command"""
        print(f"{self.name} rolled over!")