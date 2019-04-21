import pandas as pd

ASIN_list = []

# Fetching the files from the following file
with open('asin_test.txt','r') as fi:
    ASIN_list = fi.read().splitlines()

file_names = []


"""
Run this block of code to include headers to all the title metadata files.

for asin in ASIN_list:
    df = pd.read_csv(r'./review_data/'+asin+"titles_metadata.csv", header=None,
                      names=['Words_Title','Chars_Title', 'Upper_percentage', 'Lower_percentage'],
                      index_col=False)
    df.to_csv(r'./review_data/'+asin+"titles_metadata.csv", index=False)
"""

for asin in ASIN_list:
    file = './review_data/' + asin + 'titles_metadata.csv'
    file_names.append(file)
    df_list = [pd.read_csv(f) for f in file_names]
    final_df = pd.concat(df_list, ignore_index=True)

print(final_df)
print(final_df.info())
final_df.to_csv('FinalTitles.csv', index=False)
