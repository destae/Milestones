import os
import unittest
from unittest import mock
from milestone_2.src.dataframe import Dataframe

class TestDataframe(unittest.TestCase):

    def setUp(self):
        self.test_file_name = f"{os.getcwd()}/milestone_2/test/test_data.sor"
        self.schema = ['S', 'I', 'I', 'S', 'I', 'I', 'I']
        self.data_frame = Dataframe(file_name=self.test_file_name, schema=self.schema, ncols=7, nrows=5)

    def test_read_file(self):
        out_data = [['"arriba"', '2', '', '"2005-09-16"', '55', '11', '7'],
        ['"pizza"', '31490', '30', '"2002-06-17"', '30', '9', '6'],
        ['"chili"', '112140', '130', '"2005-02-25"', '130', '6', '13'],
        ['"potatoes"', '59389', '45', '"2003-04-14"', '45', '11', '11'],
        ['"ketchup"', '44061', '190', '"2002-10-25"', '190', '5', '8']]
        self.assertEqual(out_data, self.data_frame.data)
