import pandas as pd
import os
import numpy as np

class FileUtils:

    def __init__(self,csv_file):
        self.df = pd.read_csv(csv_file).fillna(0)
        self.df = self.df.loc[:, ~self.df.columns.str.contains('^Unnamed')]


    def generate_sor(self):
        new_df = self.df.astype(str)
        for col_name in self.df.columns:
            if self.df[col_name].dtype != np.int64:
                new_df[col_name] = [f"<\"{i}\">" for i in self.df[col_name]]
            else:
                new_df[col_name] = [f"<{i}>" for i in self.df[col_name]]
    
        with open('data.sor', 'w') as f:
            for row in new_df.itertuples(index=False):
                row_str = ""
                for c in row:
                    row_str += f"{c} "
                row_str = row_str[:-1]
                row_str += "\n"
                f.write(row_str)
    
            


if __name__ == "__main__":
    print(os.getcwd())
    f = FileUtils("Milestone 1/data/recipe.csv")
    f.generate_sor()