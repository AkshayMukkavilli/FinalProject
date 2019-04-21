import pandas as pd

df_reviews = pd.read_csv('FinalFeatures_latest.csv')
df_titles= pd.read_csv('FinalTitles.csv')
df_list = [df_reviews,df_titles]
final_df = pd.concat(df_list, axis=1)
print(final_df)

final_df.to_csv('Final_Features_With_Titles.csv', index=False)
