import utils
import os
from schema import *

<<<<<<< HEAD
# What is a dataframe?
    # Has a schema
    # Has a 2D array of rows and columns that contain data
    # determines the number of rows and columns from the file given
    # creates the 2D array from the information collected
    # stores the data
    
=======
>>>>>>> 5182b6159b3784c08c029b8ae107a4f7096c3810
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