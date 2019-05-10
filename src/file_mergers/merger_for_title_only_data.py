import pandas as pd

df1 = pd.read_csv(r'../../final_csv_files/FinalTitles_LatestData.csv')
print(df1.shape)
df2 = pd.read_csv(r'../../final_csv_files/OriginalFeatures(Corrected).csv')
print(df2.columns)
df1['Helpful_Votes'] = df2['Helpful_Votes']
df1['Z_Score_HelpfulVotes'] = df2['Z_Score_HelpfulVotes']
print(df1.head())
df1.to_csv(r'../../final_csv_files/TitleOnlyDataLatest.csv')