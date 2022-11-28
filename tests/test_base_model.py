#!/usr/bin/python3

import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_initialization(unittest.TestCase):
    """Testing the __init__ method of BaseModel"""
    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_uniq_ids(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_diff_created_at(self):
        o1 = BaseModel()
        sleep(0.05)
        o2 = BaseModel()
        self.assertLess(o1.created_at, o2.created_at)

    def test_diff_updated_at(self):
        o1 = BaseModel()
        sleep(0.05)
        o2 = BaseModel()
        self.assertLess(o1.updated_at, o2.updated_at)

    def test_init_with_kwargs(self):
        dt = datetime.now()
        dtiso = dt.isoformat()
