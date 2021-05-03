#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models
import os


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "created_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key != "__class__":
                    setattr(self, key, value)
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = type(self).__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.to_dict())

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dict property of: Soledad Frechou/Julian Arbini"""
        dict_returned = {}
        dict_returned["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                formatx = "%Y-%m-%dT%H:%M:%S.%f"
                dict_returned[key] = value.strftime(formatx)
            else:
                dict_returned[key] = value
        if '_sa_instance_state' in dict_returned:
            del dict_returned['_sa_instance_state']
        return dict_returned

    def delete(self):
        """Delete current instance from storage"""
        models.storage.delete(self)
