
# What is a data adapter meant to be able to do?
# It is meant to be able to:
    # open a file
    # read a file
    # determine the longest number of columns
    # determine the schema
    # generate a dataframe

import utils
from dataframe import Dataframe

class Adapter:
    def __init__(self, name):
        self.file_name = name
        self.longest_column = 0
        self.file_open()
        self.find_longest_column()
        self.schema = [None] * self.longest_column
        self.determine_schema()
        self.nrows = 0
        self.determine_number_of_rows()
        self.file_close()
        self.create_dataframe()

    ## Opens the file
    def file_open(self):
        self.data_file = open(self.file_name, 'r')

    ## Closes the file
    def file_close(self):
        self.data_file.close()

    ## Finds the longes column in the file
    def find_longest_column(self):
        self.data_file.seek(0) # reseting the pointer to the start of the file
        line = self.data_file.readline()
        while line:
            column_counter = 0
            for i in range(len(line)):
                if line[i] == '<':
                    while line[i] != '>':
                        i = i+1
                    if line[i] == '>':
                        column_counter = column_counter + 1
            if column_counter > self.longest_column:
                self.longest_column = column_counter
            line = self.data_file.readline()

    ## Determines the schema of the file
    def determine_schema(self):
        self.data_file.seek(0)
        line = self.data_file.readline()
        line_count = 0
        while line and line_count < 500:
            temp_schema = [None] * self.longest_column
            start_index = 0
            end_index = 0
            current_column = -1
            for i in range(len(line)):
                if line[i] == '<':
                    start_index = i+1
                    while line[i] != '>':
                        i = i+1
                    if line[i] == '>':
                        end_index = i
                        current_column += 1
                    temp_schema[current_column] = utils.determine_type_with_index(line, start_index, end_index)
            self.determine_hierarchy(temp_schema)
            line = self.data_file.readline()
            line_count += 1

    ## Given a schema, determines the heirarchy comparing it against the existing stored schema
    def determine_hierarchy(self, schema):
        i = 0
        for elem in schema:
            if elem == 'S':
                self.schema[i] = 'S'
            elif elem == 'F' and self.schema[i] != 'S':
                self.schema[i] = 'F'
            elif elem == 'I' and (self.schema[i] != 'S' and self.schema[i] != 'F'):
                self.schema[i] = 'I'
            elif elem == 'B' and (self.schema[i] != 'S' and self.schema[i] != 'F' and self.schema[i] != 'I'):
                self.schema[i] = 'B'
            i += 1

    ## Finds the number of rows in a file
    def determine_number_of_rows(self):
        self.data_file.seek(0)
        line = self.data_file.readline()
        while line:
            self.nrows += 1
            line = self.data_file.readline()

    ## Creates the dataframe from the read in file
    def create_dataframe(self):
        self.data = Dataframe(self.file_name, self.schema, self.longest_column, self.nrows)

    def retrieve_dataframe(self):
        return self.data