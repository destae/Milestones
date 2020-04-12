import os

class Schema:
    ## Creates a schema object: main constructor
    def __init__(self, schema_list: list, ncols: int=0,nrows: int=0):
        self.schema_list = schema_list
        self.ncols = ncols
        self.nrows = nrows

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Schema):
            return self.schema_list == other.schema_list
        if "schema_list" in other:
            return self.schema_list == other['schema_list']
        return False

    # Sets the number of rows represented in teh schema for the dataframe
    def set_nrows(self, nrows: int):
        self.nrows = nrows

    # Set the number of cols represented in the schema for the dataframe
    def set_ncols(self, ncols: int):
        self.ncols = ncols

    # Sets the schema
    def set_schema(self, sch: list):
        self.schema_list = sch

    # Retrieves the number of rows 
    def get_nrows(self):
        return self.nrows

    # Retrieves the number of columns
    def get_ncols(self):
        return self.ncols

    # Retrieves the schema
    def get_schema(self):
        return self.schema_list