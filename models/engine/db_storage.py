#!/usr/bin/python3
""" New engine DBStorage """

from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ DB class """
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiation """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        """ query on the current db session all obj """
        if cls is not None:
            new_dict = {}
            iterable = self.__session.query(cls)
            for ins in iterable:
                key = str(cls.__name__) + "." + str(ins.id)
                new_dict[key] = ins
        else:
            clases = ["User", "State", "City", "Amenity", "Place", "Review"]
            new_dict = {}
            for clase in clases:
                for ins in self.__session.query(clase):
                    key = clase + "." + str(ins.id)
                    new_dict[key] = ins
        return new_dict

    def new(self, obj):
        """ add the obj to the current db """
        self.__session.add(obj)

    def save(self):
        """ commit all changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from current db """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in db """
        Base.metadata.create_all(self.__engine)
        new_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(new_session)
        self.__session = Session()

    def close(self):
        """Calls remove() method on the private session attribute"""
        self.__session.close()
