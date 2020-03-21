import os
import unittest
from unittest import mock
from milestone_2.src.dataframe import Dataframe

class Test_Dataframe(unittest.TestCase):

    def setUp(self):
        self.test_file_name = f"{os.getcwd()}/milestone_2/test/test_data.sor"
        self.schema = []
        self.df = Dataframe(file_name=self.test_file_name, schema=self.schema, ncols=7, nrows=15)

    def test_read_file(self):
        out_data = [[],[]]
        self.assertEqual(out_data, self.df.data)
