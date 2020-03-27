
# What is a data adapter meant to be able to do?
# It is meant to be able to:
    # open a file
    # read a file
    # determine the longest number of columns
    # determine the schema
    # generate a dataframe

from milestone_3.src import utils
from milestone_3.src.dataframe import Dataframe
from milestone_3.src.schema import Schema

class Adapter:
    def __init__(self, name):
        self.file_name = name
        self.longest_column = 0
        self.file_open()
        self.find_longest_column() ## determines the longest row in the entire file (might need to change, but who knows TODO)
        self.sch = [None] * self.longest_column
        self.determine_schema() ## determines an array of values that represents part of the schema
        self.schema = Schema(self.sch) ## creates a schema object
        self.nrows = 0
        self.determine_number_of_rows() ## determines the number of total lines in the file
        self.file_close()

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
    def determine_hierarchy(self, schema_list: list):
        i = 0
        for elem in schema_list:
            if elem == 'S':
                self.sch[i] = 'S'
            elif elem == 'F' and self.sch[i] != 'S':
                self.sch[i] = 'F'
            elif elem == 'I' and (self.sch[i] != 'S' and self.sch[i] != 'F'):
                self.sch[i] = 'I'
            elif elem == 'B' and (self.sch[i] != 'S' and self.sch[i] != 'F' and self.sch[i] != 'I'):
                self.sch[i] = 'B'
            i += 1

    ## Finds the number of rows in a file
    def determine_number_of_rows(self):
        self.data_file.seek(0)
        line = self.data_file.readline()
        while line:
            self.nrows += 1
            line = self.data_file.readline()

    ## Creates the dataframe from the read in file
    def create_dataframe(self, start: int, end: int):
        ## this is where the read file should GO TODO 
        # return Dataframe(self.file_name, self.sch, self.longest_column, self.nrows)
        pass

        ## Reads the file
    def read_file(self):
        self.data_file.seTODOek(0)
        # this function needs to take in a from and len. These are lines 
        # roll until you get to the from line, and create the 2d array below until you reach the len line.
        # the while loop does not need to change, just add a new case. 
        # prior to the loop add another while loop that exits once the from line is reached. 
        line = self.data_file.readline()
        current_row = -1
        while line:
            current_row = current_row + 1
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
                        self.data[current_row][current_column] = self.extract_data(line[start_index:end_index], current_column)
            line = self.data_file.readline()

    ## Extracts the data from a set index from a given line -- and determines if the data is valid
    def extract_data(self, data, current_column):
        temp_data = utils.remove_whitespace(data)
        data_type = utils.determine_type(temp_data)
        
        if data_type == self.sch[current_column]:       
            return temp_data
        else:
            return ''