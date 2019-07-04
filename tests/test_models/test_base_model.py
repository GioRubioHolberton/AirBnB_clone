#!/usr/bin/python3
"""
BaseModel unittests
"""
import os
import unittest
import pep8
from models.base_model import BaseModel


class BaseModel_test(unittest.TestCase):
    """ testing BaseModel """

    @classmethod
    def setUp(cls):
        """ New BaseModel  """
        cls.new_model = BaseModel()

    @classmethod
    def tearDown(cls):
        """ Delete  """
        del cls.new_model
        try:
            os.remove('file.json')
        except BaseException:
            pass

    def test_pep8(self):
            """ pep8 testing """
            p8 = pep8.StyleGuide(quiet=True)
            asw = p8.check_files(['models/base_model.py'])
            self.assertEqual(asw.total_errors, 0, "Fix Style")


if __name__ == "__main__":
    unittest.main()
