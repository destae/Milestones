"""For testing the Adapter """

import os
import unittest
from milestone_3.src.adapter import Adapter
from milestone_3.src.adapter import Schema

class TestAdapter(unittest.TestCase):

    def setUp(self):
        self.test_file_name = f"{os.getcwd()}/milestone_3/test/test_data.sor"
        self.adapter = Adapter(name=self.test_file_name)

    def test_destermine_schema(self):
        """ Tests gettings schema"""
        schema_list = ['S', 'I', 'I', 'S', 'I', 'I', 'I']
        schema = Schema(schema_list)
        self.assertEqual(schema, self.adapter.schema)

    def test_find_longest_column(self):
        longest_col = 7
        self.assertEqual(longest_col, self.adapter.longest_column)