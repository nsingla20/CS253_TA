import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

iris = pd.read_csv("Iris.csv") # the iris dataset is now a Pandas DataFrame

print(iris.head())

print(iris["Species"].value_counts())


#error bars
x =[1, 2, 3, 4, 5, 6, 7]
y =[1, 2, 1, 3, 5, 4, 6]
y_error = 0.2
x_error = 0.2

plt.plot(x, y)
#plt.errorbar(x, y,yerr = y_error, fmt ='o')
plt.errorbar(x, y,xerr = x_error, fmt ='o')


plt.show()
