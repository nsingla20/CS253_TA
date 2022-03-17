import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

iris = pd.read_csv("Iris.csv") # the iris dataset is now a Pandas DataFrame

print(iris.head())

#lineplot
#sns.lineplot(iris['SepalWidthCm'], iris['SepalLengthCm'])
sns.lineplot(iris['PetalLengthCm'], iris['SepalLengthCm'])
plt.show()


