import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

iris = pd.read_csv("Iris.csv") # the iris dataset is now a Pandas DataFrame

print(iris.head())

print(iris["Species"].value_counts())


# box plot illustration

#sns.boxplot(x='Species', y='SepalLengthCm', data=iris)
#sns.violinplot(x='Species', y='SepalLengthCm', data=iris)
iris.drop("Id", axis=1).boxplot(by="Species")
plt.show()
