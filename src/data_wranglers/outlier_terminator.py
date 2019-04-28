import pandas as pd

df = pd.read_csv('Final_Features_With_Titles.csv')

df = df[df['Helpful Votes'] < 100]

df['Classes'] = pd.cut(df['Helpful Votes'], bins=[-1, 0, 20, 100], include_lowest=True, labels=['Useless', 'Helpful', 'Very Helpful'])
df2 = pd.DataFrame({'Votes': df['Helpful Votes'], 'Label': df['Classes']})
print(df2)

