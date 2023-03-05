#место для твоего кода
#Гипотеза: фильмы которые длятся дольше 2.5 часов имеют рейтинг больше чем у фильмов которые длятся меньше 2.5 часов
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('IMDB-Movie-Data.csv')

df['Runtime (Minutes)'].fillna(0, inplace = True)
df['Rating'].fillna(0, inplace = True)


rt1 = df[(df['Runtime (Minutes)'] > 150)]['Rating'].mean()
rt2 = df[(df['Runtime (Minutes)'] < 150)]['Rating'].mean()

s = pd.Series(data = [rt1, rt2],
index = ['Долгие фильмы', 'Короткие фильмы'])
s.plot(kind = 'bar')
plt.show()

#print(df.dropna().head(60))
