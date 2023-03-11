import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
import seaborn as sns

from sklearn.linear_model import LogisticRegression

# Read in the data
data = pd.read_csv("data.csv")
x = data[["Living_area"]]
y = data["Selling_price"]
model = LinearRegression()
# Train the model using the data
model = model.fit(x, y)
prediction = model.predict(x)
plt.xlabel("Living area (m^2)", fontsize=18)
plt.ylabel("Selling price MSEK", fontsize=18)
# Show the graph
plt.scatter(x, y)
plt.plot(x, prediction , color='black')
plt.show()

# Load dataset
iris = datasets.load_iris()

# Split dataset into training set and test set
x_train , x_test, y_train , y_test = train_test_split(
iris.data, iris.target, test_size=0.25, random_state=0)
logisticRegr = LogisticRegression(multi_class='ovr', solver='liblinear')
logisticRegr.fit(x_train , y_train)

# Make predictions on entire test data
predictions = logisticRegr.predict(x_test)

# Use the score method to get the accuracy of model
score = logisticRegr.score(x_test, y_test)
cm = metrics.confusion_matrix(y_test, predictions)

plt.figure(figsize=(9, 9))
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5,
square=True, cmap='Blues_r', xticklabels=iris.target_names ,
yticklabels=iris.target_names)
all_sample_title = 'Accuracy Score: {0}'.format(score)
plt.title(all_sample_title , size=15)
plt.show()


iris = datasets.load_iris()

# Split dataset into training set and test set
x_train , x_test, y_train , y_test = train_test_split(
iris.data, iris.target, test_size=0.25, random_state=0)
kVals = [1, 15, 34, 51, 80, 100]
for i in range(len(kVals)*2):

# Determine k and weight type
    k = kVals[i // 2]
    weight = 'uniform' if (i % 2 == 0) else 'distance'

    # Create KNN Classifier
    knn = KNeighborsClassifier(n_neighbors=k, weights=weight)
    knn.fit(x_train , y_train)

    # classifier eval
    predictions = knn.predict(x_test)
    score = knn.score(x_test, y_test)
    confMatrix = metrics.confusion_matrix(y_test, predictions)

    # Plot
    title = ' Accuracy Score: {0}'.format(score) + '\n K Value = {0}'.format(k) + ', {0} '.format(weight)+ 'weighted'
    sns.heatmap(confMatrix , annot=True, fmt=".3f", linewidths=0.5,
    square=True,
    cmap='Blues_r', xticklabels=iris.target_names ,
    yticklabels=iris.target_names)
    plt.title(title, size=15)
    plt.show()

