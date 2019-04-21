import pandas as pd

ASIN_list = []
with open('asin_test.txt', 'r', encoding='utf-8') as fi:
    ASIN_list = fi.read().splitlines()
print(ASIN_list)
file_names = []
print(file_names)
print(type(file_names))
for asin in ASIN_list:
    print(f"ASIN is {asin}")
    file = './review_data_sentiments/' + asin + 'metadata.csv'
    print(file)
    print(type(file))
    file_names.append(file)
    print(file_names)
df_list = [pd.read_csv(f) for f in file_names]
final_df = pd.concat(df_list, ignore_index=True)
print(final_df)
print(final_df.info())
final_df.to_csv('Features_Sentiments.csv', index=False)

