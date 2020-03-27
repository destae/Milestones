import os
import unittest
from unittest import mock
from milestone_3.src.dataframe import Dataframe
from milestone_3.src.adapter import Schema


class TestDataframe(unittest.TestCase):

    def setUp(self):
        self.test_file_name = f"{os.getcwd()}/milestone_2/test/test_data.sor"
        self.data = [['arriba', 2, 1, '2005-09-16', 55, 11, 7],
        ['pizza', 31490, 30, '2002-06-17', 30, 9, 6],
        ['chili', 112140, 130, '2005-02-25', 130, 6, 13],
        ['potatoes', 59389, 45, '2003-04-14', 45, 11, 11],
        ['ketchup', 44061, 190, '2002-10-25', 190, 5, 8]]
        self.schema = Schema(sch=['S', 'I', 'I', 'S', 'I', 'I', 'I'],ncols=7,nrows=5)
        self.data_frame = Dataframe(sch=self.schema,data=self.data)

    def test_get_nrows(self):
        self.assertEqual(5, self.data_frame.get_nrows())

    def test_get_ncols(self):
        self.assertEqual(7, self.data_frame.get_ncols())

    def test_get_value_0(self):
        self.assertEqual("arriba", self.data_frame.get_value(0,0)) 

    def test_get_value_1(self):
       self.assertEqual(31490, self.data_frame.get_value(1,1))
      
    def test_get_value_2(self):
        self.assertEqual(130, self.data_frame.get_value(2,2))

    def test_get_value_3(self):
        self.assertEqual('2003-04-14', self.data_frame.get_value(3,3))

    def test_dataframe_to_string(self):
        self.assertEqual( "['arriba', 2, 1, '2005-09-16', 55, 11, 7]\n"
                        + "['pizza', 31490, 30, '2002-06-17', 30, 9, 6]\n"
                        + "['chili', 112140, 130, '2005-02-25', 130, 6, 13]\n"
                        + "['potatoes', 59389, 45, '2003-04-14', 45, 11, 11]\n"
                        + "['ketchup', 44061, 190, '2002-10-25', 190, 5, 8]\n",
        self.data_frame.dataframe_to_string())

 