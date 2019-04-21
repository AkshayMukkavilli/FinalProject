import pandas as pd

data_1 = pd.read_csv('FinalFeatures.csv')
data_2 = pd.read_csv('FinalFeatures_1.csv')

data_final = pd.concat([data_1,data_2])
print(data_final.info())