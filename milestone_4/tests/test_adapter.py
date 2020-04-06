"""For testing the Adapter """

import os
import unittest
from milestone_4.src.adapter import Adapter
from milestone_4.src.adapter import Schema

class TestAdapter(unittest.TestCase):

    def setUp(self):
        self.test_file_name = f"{os.getcwd()}/milestone_4/tests/test_data.sor"
        self.adapter = Adapter(name=self.test_file_name)

    def test_destermine_schema(self):
        """ Tests gettings schema"""
        schema_list = ['S', 'I', 'I', 'S', 'I', 'I', 'I']
        schema = Schema(schema_list)
        self.assertEqual(schema, self.adapter.schema)

    def test_find_longest_column(self):
        longest_col = 7
        self.assertEqual(longest_col, self.adapter.longest_column)

    def test_determine_number_of_rows(self):
        nrows = 5
        self.assertEqual(nrows, self.adapter.nrows)

    def test_determine_number_of_rows2(self):
        row_file = f"{os.getcwd()}/milestone_4/tests/less_rows.sor"
        adapter = Adapter(name=row_file)
        self.assertEqual(5,adapter.nrows) # TODO This says 5 even though the last row is not complete... idk if this is okay???
    
    