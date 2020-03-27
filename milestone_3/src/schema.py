import os


class Schema:

    def __init__(self, sch: list, ncols: int=0,nrows: int=0):
        self.schema_list = sch
        self.ncols = ncols
        self.nrows = nrows

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Schema):
            return self.schema_list == other.schema_list
        return False

    def set_nrows(self, nrows: int):
        self.nrows = nrows

    def set_ncols(self, ncols: int):
        self.ncols = ncols

    def set_schema(self, sch: list):
        self.schema_list = sch

    def get_nrows(self):
        return self.nrows

    def get_ncols(self):
        return self.ncols

    def get_schema(self):
        return self.schema_list