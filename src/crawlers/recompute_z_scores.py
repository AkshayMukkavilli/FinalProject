import pandas as pd

ASIN_list = []

with open('asin_test.txt','r') as fi:
    ASIN_list = fi.read().splitlines()

for asin in ASIN_list:
    with open('./review_data_sentiments/'+asin+'metadata.csv', 'r', encoding='utf-8') as fr:
        df = pd.read_csv('./review_data_sentiments/'+asin+'metadata.csv')
        df.drop(columns=['Z_Score_HelpfulVotes'], inplace=True)
        df['Z_Score_HelpfulVotes'] = (df['Helpful_Votes'] - df['Helpful_Votes'].mean()) / df['Helpful_Votes'].std(
            ddof=0)
        df.to_csv('./review_data_sentiments/'+asin+'metadata.csv', index=False, header=True)
