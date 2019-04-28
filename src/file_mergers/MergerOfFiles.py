"""
Module used to merge all the csv files.
Each product on Amazon has a unique ASIN number. We have been storing 4 different files for each ASIN number.
With this module, we can merge all the necessary files into one csv file
that we can use for Machine Learning Techniques.
"""
import pandas as pd


def merge_files(output_file_name):
    with open('../asins/asin_test.txt', 'r', encoding='utf-8') as asin_reader:
        ASIN_list = asin_reader.read().splitlines()
    file_names = []
    for each_asin in ASIN_list:
        each_file = '../data/review_data_sentiments/' + each_asin + 'titles_metadata.csv'
        file_names.append(each_file)
    list_of_dfs = [pd.read_csv(file_name) for file_name in file_names]
    merged_df = pd.concat(list_of_dfs, ignore_index=True)
    merged_df.to_csv("../../final_csv_files" + output_file_name, index=False)

# merge_files()








