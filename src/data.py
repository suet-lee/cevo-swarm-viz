from pathlib import Path
import os
import json
import pandas as pd
import ast

class Data:

    def __init__(self, filepath, is_coords=True, r_phase=False):
        self.data = self.read_file_csv(filepath, is_coords, r_phase)

    def read_file_csv(self, filepath, is_coords=True, r_phase=False):
        d = pd.read_csv(filepath)
        if r_phase:
            d = d.transpose()
        
        d_ = json.loads(d.to_json())
        data = []
        for ts, val in d_.items():
            v = val.values()
            if is_coords:
                v_ = []
                for it in v:
                    v_.append(ast.literal_eval(it))
                data.append(v_)
            else:
                data.append(list(v))
        return data

    # def read_file(self, filepath, read_as_dict=False):
    #     with open(filepath, 'r') as f:
    #         data = f.readlines()

    #     data_ = []
    #     for it in data:
    #         try:
    #             row = json.loads(it.strip())
    #         except:
    #             row = []
                
    #         if type(row) is dict and not read_as_dict:
    #             data_.append(list(row.values()))
    #         else:
    #             data_.append(row)
        
    #     return data_
