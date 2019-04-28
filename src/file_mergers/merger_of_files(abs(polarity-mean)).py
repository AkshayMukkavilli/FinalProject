import pandas as pd
import numpy as np

ASIN_list = []
with open("/Users/t_velpac/mission/WorkingCopy/src/asins/asin_test.txt", 'r', encoding='utf-8') as fi:
    ASIN_list = fi.read().splitlines()
print(ASIN_list)
file_names = []
print(file_names)
print(type(file_names))
for asin in ASIN_list:
    file = '../data/review_data_sentiments/' + asin + 'metadata.csv'
    file_names.append(file)
df_list = [pd.read_csv(f) for f in file_names]

# Calculating the Absolute value of (Sentiment Polarity - mean(Sentiment Polarity)), merge
# the files and store them as a new csv file
for df in df_list:
    df['Absolute(Sentiment-Mean)'] = abs(df['Sentiment_Polarity'] - np.mean(df['Sentiment_Polarity']))


final_df = pd.concat(df_list, ignore_index=True)
print(final_df)
print(final_df.info())
final_df.to_csv("../../final_csv_files/Abs_Sentiment-Mean.csv", index=False)