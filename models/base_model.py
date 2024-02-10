#!/usr/bin/python3
"""
BaseModel Module Definition
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class definition
    """
    def __init__(self):
        """ BaseModel initialisation """
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        """
        string representation
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
