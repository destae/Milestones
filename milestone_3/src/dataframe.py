import utils
import os
from schema import *

class Dataframe:
    def __init__(self, data: list, sch: Schema:
        self.schema = sch
        self.ncols = sch.get_ncols()
        self.nrows = sch.get_nrows()
        self.data = data
    
    ## Retrieves the number of rows of the dataframe
    def get_nrows(self):
        return self.nrows

    ## Retrives the number of columns of the dataframe
    def get_ncols(self):
        return self.ncols

    ## Gets the raw value of the data stored at the given coordinates
    def get_value(self, col: int, row: int):
        if (col < self.ncols and col >= 0 and row >= 0 and row < self.nrows):
            return self.data[row][col]

    ## Returns the type of of the value stored at the given coordinates
    def get_type(self, col: int, row: int):
        if (col < self.ncols and col >= 0 and row >= 0 and row < self.nrows):
            return sch.get_schema()[col]

    ## Constructs a string from the dataframe
    def dataframe_to_string(self):
        tmp_string = ""
        for row in self.data:
            tmp_string += "".join(
                [ c for c in str(row) if c not in ('(', ')','[',']',',')]
            )
            tmp_string += "\n"
        return tmp_string