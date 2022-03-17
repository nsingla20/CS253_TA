import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

iris = pd.read_csv("Iris.csv") # the iris dataset is now a Pandas DataFrame

print(iris.head())

print(iris["Species"].value_counts())


#piechart
#label=['Iris-setosa','Iris-versicolor','Iris-virginica']
cnt=iris["Species"].value_counts()
label=[cnt['Iris-setosa'],cnt['Iris-versicolor'],cnt['Iris-virginica']]
plt.pie(cnt, labels=label)

plt.show()
