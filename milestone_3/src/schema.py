import os

class Schema:
    def __init__(self, sch: list)
        self.schema_list = sch
        self.ncols = 0
        self.nrows = 0


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