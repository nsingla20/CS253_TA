import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

iris = pd.read_csv("Iris.csv") # the iris dataset is now a Pandas DataFrame

print(iris.head())

print(iris["Species"].value_counts())

#lineplot
#sns.lineplot(iris['SepalWidthCm'], iris['SepalLengthCm'])



# scatter plot illustration
'''
Scatter plots or scatter graphs is a bivariate plot having greater resemblance to line graphs in the way they are built. A line graph uses a line on an X-Y axis to plot a continuous function, while a scatter plot relies on dots to represent individual pieces of data. These plots are very useful to see if two variables are correlated. Scatter plot could be 2 dimensional or 3 dimensional.

Displays correlation between variables
Suitable for large data sets
Easier to find data clusters
'''
#plt.scatter(iris['SepalLengthCm'], iris['SepalWidthCm'])
#plt.scatter(iris['SepalLengthCm'], iris['Species'])
#plt.scatter(iris['PetalLengthCm'], iris['PetalWidthCm'])
#iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm") # using pandas
#sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, size=5) 

# box plot illustration
# nice visual representation when it comes to measuring the data distribution.

#sns.boxplot(x='Species', y='SepalWidthCm', data=iris)
#sns.violinplot(x='Species', y='SepalWidthCm', data=iris)
# Now that we've covered seaborn, let's go back to some of the ones we can make with Pandas
# We can quickly make a boxplot with Pandas on each feature split out by species
#iris.drop("Id", axis=1).boxplot(by="Species")

# illustrate histogram
#features = ['SepalWidthCm', 'PetalWidthCm']
#iris[features].hist(figsize=(10, 4))



# illustrate count plots
#sns.countplot(x='Species', data=iris)
#sns.countplot(x='SepalWidthCm', data=iris)


# illustrate heat map.
#sns.heatmap(iris.select_dtypes(include='number').corr(),
#			cmap=sns.cubehelix_palette(20, light=0.95, dark=0.15))

#piechart
#label=['Iris-setosa','Iris-versicolor','Iris-virginica']
#cnt=iris["Species"].value_counts()
#label==[cnt['Iris-setosa'],cnt['Iris-versicolor'],cnt['Iris-virginica']]
#plt.pie(cnt, labels=label)


#error bars
'''
x =[1, 2, 3, 4, 5, 6, 7]
y =[1, 2, 1, 3, 5, 4, 6]
y_error = 0.2
x_error = 0.2

plt.plot(x, y)
#plt.errorbar(x, y,yerr = y_error, fmt ='o')
plt.errorbar(x, y,xerr = x_error, fmt ='o')
'''

# Another useful seaborn plot is the pairplot, which shows the bivariate relation
# between each pair of features
# From the pairplot, we'll see that the Iris-setosa species is separataed from the other
# two across all feature combinations
#sns.pairplot(iris.drop("Id", axis=1), hue="Species", size=3)



plt.show()
