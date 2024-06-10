#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""

    def test_get(self):
        """Test getting a User"""
        user = self.storage.get(User, 'user1')
        self.assertEqual(user.id, 'user1')
        self.assertEqual(user.name, 'user1')

        """Test getting a State"""
        state = self.storage.get(State, 'state1')
        self.assertEqual(state.id, 'state1')
        self.assertEqual(state.name, 'state1')

        """Test getting a City"""
        city = self.storage.get(City, 'city1')
        self.assertEqual(city.id, 'city1')
        self.assertEqual(city.name, 'city1')

        """Test getting an Amenity"""
        amenity = self.storage.get(Amenity, 'amenity1')
        self.assertEqual(amenity.id, 'amenity1')
        self.assertEqual(amenity.name, 'amenity1')

        """Test getting a Place"""
        place = self.storage.get(Place, 'place1')
        self.assertEqual(place.id, 'place1')
        self.assertEqual(place.name, 'place1')

        """Test getting a Review"""
        review = self.storage.get(Review, 'review1')
        self.assertEqual(review.id, 'review1')
        self.assertEqual(review.text, 'review1')

        """Test getting a non-existent object"""
        self.assertIsNone(self.storage.get(User, 'non_existent'))

    def test_count(self):
        """Test counting all objects"""
        self.assertEqual(self.storage.count(), 12)

        """Test counting objects of a specific class"""
        self.assertEqual(self.storage.count(User), 2)
        self.assertEqual(self.storage.count(State), 2)
        self.assertEqual(self.storage.count(City), 2)
        self.assertEqual(self.storage.count(Amenity), 2)
        self.assertEqual(self.storage.count(Place), 2)
        self.assertEqual(self.storage.count(Review), 2)

        """Test counting objects of a non-existent class"""
        self.assertEqual(self.storage.count(Mock), 0)
