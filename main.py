import pandas as pd
import matplotlib.pyplot as plt
dat = pd.read_csv("Акции Сбера и нефть в рублях.csv")
dat['Дата'] = pd.to_datetime(dat['Дата'])
dat.index = dat['Дата']
dat['Year'] = dat.index.year
dat['Mon'] = dat.index.month
dat['Day'] = dat.index.day
dates = dat[['Year','Mon','Day']]
dat.index = pd.MultiIndex.from_tuples(dates.values.tolist(), names=dates.columns)

corr = dat['Цена акции SBER'].corr(dat['Цена нефти BRENT'], method='pearson')
plt.imshow(corr,cmap='seismic',interpolation='none',vmin=-1,vmax=1)
plt.colorbar()
plt.xticks(range(len(corr)),corr.columns)
plt.yticks(range(len(corr)),corr.columns)
print(f"Pearson correlation: {corr:.3f}")
