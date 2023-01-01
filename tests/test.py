#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.bm = BaseModel()

    def test_init(self):
        # Test that the id, created_at, and updated_at attributes are set correctly
        self.assertIsInstance(self.bm.id, str)
        self.assertIsInstance(self.bm.created_at, datetime)
        self.assertIsInstance(self.bm.updated_at, datetime)
        self.assertEqual(self.bm.created_at, self.bm.updated_at)

        # Test that the object is added to the storage list
        self.assertIn(self.bm, BaseModel.storage)

    def test_str(self):
        # Test that the __str__ method returns the correct string
        expected = "[BaseModel] ({}) {}".format(self.bm.id, self.bm.__dict__)
        self.assertEqual(str(self.bm), expected)

    def test_save(self):
        # Test that the save method updates the updated_at attribute
        before = self.bm.updated_at
        self.bm.save()
        after = self.bm.updated_at
        self.assertNotEqual(before, after)

    def test_to_dict(self):
        # Test that the to_dict method returns the correct dictionary
        expected = {
            "id": self.bm.id,
            "__class__": "BaseModel",
            "created_at": self.bm.created_at.isoformat(),
            "updated_at": self.bm.updated_at.isoformat()
        }
        self.assertEqual(self.bm.to_dict(), expected)

if __name__ == '__main__':
    unittest.main()

