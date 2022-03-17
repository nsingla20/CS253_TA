import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

iris = pd.read_csv("Iris.csv") # the iris dataset is now a Pandas DataFrame

print(iris.head())



#plt.scatter(iris['SepalWidthCm'], iris['SepalLengthCm'])
#plt.scatter(iris['Species'],iris['SepalLengthCm'])
#plt.scatter(iris['PetalLengthCm'], iris['PetalWidthCm'])
#iris.plot(kind="scatter", x="SepalWidthCm", y="SepalLengthCm") # using pandas
sns.jointplot(x="SepalWidthCm", y="SepalLengthCm", data=iris, size=5) 
#plt.xlabel('Species')
#plt.ylabel('SepalLength')
plt.show()
