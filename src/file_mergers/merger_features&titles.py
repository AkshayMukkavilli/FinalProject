import pandas as pd

df_reviews = pd.read_csv("../../final_csv_files/OriginalFeatures(Corrected).csv")
df_titles = pd.read_csv("../../final_csv_files/FinalTitles_LatestData.csv")
df_list = [df_reviews,df_titles]
final_df = pd.concat(df_list, axis=1)
print(final_df)
print(final_df.columns)

final_df.to_csv("../../final_csv_files/Final_Features_With_Titles(Latest_Data).csv", index=False)
