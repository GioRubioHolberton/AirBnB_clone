#!/usr/bin/python3

from datetime import datetime
import uuid
import models

class BaseModel:
    'Base class created. It inherates the base data'

    def __init__(self):
        'Constructor for the BaseModel Class. COntains the basics to the future classes'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        'String representation for instances'
        return("[{}] ({}) <{}>".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        'Savind date and time for each update'
        self.updated_at = datetime.now()

    def to_dict(self):
        'Converts the object on a dictionary'
        for keys, values in self.__dict__.items():
            if keys == "created_at" or keys == "updated_at":
                values = datetime.now().isoformat()
                setattr(self, keys, values)
            setattr(self, keys, values)
            ob_to_dict = self.__dict__.copy()
            ob_to_dict["__class__"] = self.__class__.__name__
        return ob_to_dict
