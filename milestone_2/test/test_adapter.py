"""For testing the Adapter """

import os
import unittest
from unittest import mock
from milestone_2.src.adapter import Adapter


class Test_Adapter(unittest.TestCase):
    """This is a docstring """

    def setUp(self):
        self.test_file_name = f"{os.getcwd()}/milestone_2/test/test_data.sor"
        self.adapter = Adapter(name=self.test_file_name)

    def test_destermine_schema(self):
        """ Tests gettings schema"""
                
        schema = [[], []]
        self.assertEqual(schema, self.adapter.schema)
