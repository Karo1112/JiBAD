import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv("Plant_1_Generation_Data.csv")
df2 = pd.read_csv("Plant_2_Generation_Data.csv")
df2['DATE_TIME'] = df2['DATE_TIME'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
df2['DATE_TIME'] = df2['DATE_TIME'].apply(lambda x: datetime.strftime(x, '%d-%m-%Y %H:%M:%S'))
dataframe = [df1, df2]
dataframe = pd.concat(dataframe, ignore_index=True)
dataframe = dataframe.dropna()
dataframe['DATE_TIME'] = pd.to_datetime(dataframe['DATE_TIME'])
week = dataframe.loc[(dataframe['DATE_TIME'] >= '15-05-2020 00:00') & (dataframe['DATE_TIME'] < '22-05-2020 00:00')]
print(week)
week_source = week.loc[week['SOURCE_KEY'] == '7JYdWkrLSPkdwr4']
week1 = week_source['DATE_TIME']
ac_power = week_source['AC_POWER']
plt.plot(week1, ac_power, label='konkretny generator') #wykres1
#plt.show()
wykres2 = week[['DATE_TIME', 'AC_POWER']]
wykres2 = wykres2.groupby('DATE_TIME')['AC_POWER'].mean().reset_index()
print(wykres2)
plt.plot(wykres2['DATE_TIME'], wykres2['AC_POWER'], label='srednia')
plt.legend()
plt.show()

#podpunkt 5
srednie = dataframe[['DATE_TIME', 'AC_POWER']]
srednie['srednie'] = srednie.groupby('DATE_TIME')['AC_POWER'].transform(np.average)
przypadki = dataframe[['DATE_TIME', 'SOURCE_KEY']].where((dataframe['AC_POWER'] < 0.8 * srednie['srednie']))
przypadki.dropna()
print(przypadki['SOURCE_KEY'].value_counts())