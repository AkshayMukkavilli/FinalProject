import os
import sys
from final_csv_files.__init__ import path_to_final_csvs

# class path_requirements:
#     """
#     Contains methods that can perform path manipulations on any operating systems
#     """
#
#     def __init__(self):
#         """
#         Defines the path names for all important directories
#         """
#         self.path_to_final_csv_files = os.


import pandas as pd

dataset = pd.read_csv(r'C:\Users\aksha\PycharmProjects\FinalProject\final_csv_files\Abs_Sentiment-Mean.csv')
dataset.drop(columns=['Date', 'Stars'])
print(dataset.head())


