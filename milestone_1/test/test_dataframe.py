import os
import src
from src.dataframe import Dataframe
import unittest
from unittest import mock

class TestDataframe(unittest.TestCase):

    def setUp(self):
        self.test_file_name = "/home/lucas/code/sd/final_project/Milestone 1/test/test_data.sor"
        self.schema = mock.MagicMock()
        self.df = Dataframe(file_name=self.test_file_name,schema=self.schema,ncols=7,nrows=15)

    def test_read_file(self):
        out_data = [[],[]]
        self.assertEqual(out_data,self.df.data)


if __name__ == "__main__":
    unittest.main()

