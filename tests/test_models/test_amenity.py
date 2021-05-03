#!/usr/bin/python3
""" testing """
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class test_amenity_two(unittest.TestCase):
    """  xdxdxd  """
    @classmethod
    def setUpClass(cls):
        """  xdxdxd  """
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """  xdxdxd  """
        del cls.amenity

    def tearDown(self):
        """  xdxdxd  """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Amenity(self):
        """"  xdxdxd  """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "pep8 error")

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "Filestorage")
    def test_save_Amenity(self):
        """  xdxdxd  """
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_Amenity(self):
        """  xdxdxd  """
        self.assertEqual('to_dict' in dir(self.amenity), True)


    def test_checking_for_docstring_Amenity(self):
        """  xdxdxd  """
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_Amenity(self):
        """  xdxdxd  """
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_is_subclass_Amenity(self):
        """  xdxdxd  """
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types_Amenity(self):
        """  xdxdxd  """
        self.assertEqual(type(self.amenity.name), str)

if __name__ == "__main__":
    unittest.main()
