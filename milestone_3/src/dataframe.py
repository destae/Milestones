import utils
import os

# What is a dataframe?
    # Has a schema
    # Has a 2D array of rows and columns that contain data
    # determines the number of rows and columns from the file given
    # creates the 2D array from the information collected
    # stores the data
class Dataframe:
    def __init__(self, file_name: str, schema, ncols: int, nrows: int):
        self.file_name = file_name
        self.schema = schema
        self.ncols = ncols
        self.nrows = nrows
        self.data = [['' for x in range(self.ncols)] for y in range(self.nrows)]
        self.file_open()
        self.read_file()
        self.file_close()
    
    def get_nrows(self):
        return self.nrows

    def get_ncols(self):
        return self.ncols

    ## Opens the file
    def file_open(self):
        self.data_file = open(self.file_name,'r')

    ## Closes the file
    def file_close(self):
        self.data_file.close()

    ## Reads the file
    def read_file(self):
        self.data_file.seek(0)
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
        
        if data_type == self.schema[current_column]:       
            return temp_data
        else:
            return ''

    def dataframe_to_string(self):
        tmp_string = ""
        for row in self.data:
            tmp_string += "".join(
                [ c for c in str(row) if c not in ('(', ')','[',']',',')]
            )
            tmp_string += "\n"
        return tmp_string