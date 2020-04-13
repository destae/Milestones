import os
import unittest
import json
from unittest import mock
from verify.src.dataframe import Dataframe
from verify.src.schema import Schema
from verify.src.kv_store import Key, KeyValueStore


class TestDataframe(unittest.TestCase):

    def setUp(self):
        self.test_file_name = f"{os.getcwd()}/verifyS/tests/test_data.sor"
        self.data = [['arriba', 2, 1, '2005-09-16', 55, 11, 7],
        ['pizza', 31490, 30, '2002-06-17', 30, 9, 6],
        ['chili', 112140, 130, '2005-02-25', 130, 6, 13],
        ['potatoes', 59389, 45, '2003-04-14', 45, 11, 11],
        ['ketchup', 44061, 190, '2002-10-25', 190, 5, 8]]
        self.schema = Schema(schema_list=['S', 'I', 'I', 'S', 'I', 'I', 'I'],ncols=7,nrows=5)
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

    def test_dataframe_from_array(self):
        vals = [float(i) for i in range(0,500)]
        key = Key("test",0)
        kv = KeyValueStore()
        d = Dataframe.from_array(key=key,kv=kv, size=500,array=vals,arr_type='F')
        test_schema = Schema(schema_list=["F"],ncols=1,nrows=500)
        self.assertEqual(test_schema, d.schema)

    def test_dataframe_from_array2(self):
        vals = [float(i) for i in range(0,5)]
        key = Key("test",0)
        kv = KeyValueStore()
        d = Dataframe.from_array(key=key,kv=kv,size=5,array=vals,arr_type='F')
        self.assertEqual([vals], d.data)
 
    def test_dataframe_from_scalar(self):
        vals = [float(i) for i in range(0,5)]
        sum_vals=float(sum(vals))
        key = Key("test",0)
        kv = KeyValueStore()
        d = Dataframe.from_scalar(key=key,kv=kv, scalar=sum_vals, scalar_type='F')
        self.assertEqual(Schema(schema_list=["F"],ncols=1,nrows=1), d.schema)

    def test_dataframe_from_scalar2(self):
        vals = [float(i) for i in range(0,5)]
        sum_vals = float(sum(vals))
        key = Key("test",0)
        kv = KeyValueStore()
        d = Dataframe.from_scalar(key=key,kv=kv, scalar=sum_vals,scalar_type='F')
        self.assertEqual(sum_vals, d.get_value(0,0))
 
    def test_dataframe_to_json(self):
        test_dict ={"schema": {"schema_list": ["S", "I", "I", "S", "I", "I", "I"], "ncols": 7, "nrows": 5}, "ncols": 7, "nrows": 5, "data": [["arriba", 2, 1, "2005-09-16", 55, 11, 7], ["pizza", 31490, 30, "2002-06-17", 30, 9, 6], ["chili", 112140, 130, "2005-02-25", 130, 6, 13], ["potatoes", 59389, 45, "2003-04-14", 45, 11, 11], ["ketchup", 44061, 190, "2002-10-25", 190, 5, 8]]}
        self.assertEqual(self.data_frame.serialize(), json.dumps(test_dict))


    def test_dataframe_to_json2(self):
        vals = [float(i) for i in range(0,5)]
        key = Key("test",0)
        kv = KeyValueStore()
        d = Dataframe.from_array(key=key,kv=kv,size=5,array=vals,arr_type='F')
        str_df = d.serialize()
        self.assertEqual(str_df, 
        json.dumps({"schema": {"schema_list": ["F"], "ncols": 1, "nrows": 5}, "ncols": 1, "nrows": 5, "data": [[0.0, 1.0, 2.0, 3.0, 4.0]]}))
 
    def test_json_to_dataframe(self):
        test_dict ={"schema": {"schema_list": ["S", "I", "I", "S", "I", "I", "I"], "ncols": 7, "nrows": 5}, "ncols": 7, "nrows": 5, "data": [["arriba", 2, 1, "2005-09-16", 55, 11, 7], ["pizza", 31490, 30, "2002-06-17", 30, 9, 6], ["chili", 112140, 130, "2005-02-25", 130, 6, 13], ["potatoes", 59389, 45, "2003-04-14", 45, 11, 11], ["ketchup", 44061, 190, "2002-10-25", 190, 5, 8]]}
        json_df = json.dumps(test_dict)
        self.assertEqual(self.data_frame.data, Dataframe.from_json(json_df).data)


    def test_json_to_dataframe2(self):
        vals = [float(i) for i in range(0,5)]
        key = Key("test",0)
        kv = KeyValueStore()
        d = Dataframe.from_array(key=key,kv=kv,size=5,array=vals,arr_type='F')
        str_df = d.serialize()
        json_df = json.dumps({"schema": {"schema_list": ["F"], "ncols": 1, "nrows": 5}, "ncols": 1, "nrows": 5, "data": [[0.0, 1.0, 2.0, 3.0, 4.0]]})
        test_dataframe = Dataframe.from_json(json_df)
        self.assertEqual(d, test_dataframe) 
