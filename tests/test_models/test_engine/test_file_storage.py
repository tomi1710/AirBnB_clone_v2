#!/usr/bin/python3
""" testing """
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') == 'db',
    "This test only work in Filestorage")
class TestFileStorage(unittest.TestCase):
    """ testing """

    @classmethod
    def setUpClass(cls):
        """ testing """
        cls.user = User()
        cls.user.first_name = "mesa"
        cls.user.last_name = "diez"
        cls.user.email = "hbtn@coreo.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """ testing """
        del cls.user

    def tearDown(self):
        """ testing """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """ testing """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "pep8 errors")

    def test_all(self):
        """ testing """
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """ testing """
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.name = "holberton"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload_filestorage(self):
        """ testing """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")

        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except Exception:
            pass

        self.storage.save()

        with open(path, 'r') as f:
            lines2 = f.readlines()

        self.assertEqual(lines, lines2)

        try:
            os.remove(path)
        except Exception:
            pass

        with open(path, "w") as f:
            f.write("{}")

        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")

        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
