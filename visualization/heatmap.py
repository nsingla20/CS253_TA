import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

iris = pd.read_csv("Iris.csv") # the iris dataset is now a Pandas DataFrame

print(iris.head())

print(iris["Species"].value_counts())

# illustrate heat map.
sns.heatmap(iris.select_dtypes(include='number').corr(),
			cmap=sns.cubehelix_palette(20, light=0.95, dark=0.15))


plt.show()
