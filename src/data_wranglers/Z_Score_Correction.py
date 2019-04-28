import pandas as pd

# df = pd.read_csv(r'/Users/t_velpac/mission/WorkingCopy/FinalFeatures_latest.csv')
df = pd.read_csv(r"/Users/t_velpac/mission/WorkingCopy/final_csv_files/Final_Features_With_Titles.csv")
df.drop(columns='Z_Score_HelpfulVotes', inplace=True)
print(df.columns)
df['Z_Score_HelpfulVotes'] = (df['Helpful Votes'] - df['Helpful Votes'].mean()) / df['Helpful Votes'].std(ddof=0)
df.to_csv(r"/Users/t_velpac/mission/WorkingCopy/final_csv_files/Final_Features_With_Titles.csv", index=False)
