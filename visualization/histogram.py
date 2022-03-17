import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

iris = pd.read_csv("Iris.csv") # the iris dataset is now a Pandas DataFrame

print(iris.head())

print(iris["Species"].value_counts())


# illustrate histogram
features = ['SepalWidthCm', 'SepalLengthCm']
iris[features].hist(figsize=(10, 4))
plt.show()


