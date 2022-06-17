"""Use SGDClassifier.

使用scilit-learn的SGDClassifier類別，實作Perceptron、Logistic Regression、
Support Vector Machine演算法。
"""
import numpy as np
from plot_decision_regions import plot_decision_regions
from sklearn import datasets
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris()

x_data = iris.data[:, [2, 3]]
y_data = iris.target

x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size=0.2, random_state=0)

sc = StandardScaler()
sc.fit(x_train)
x_train_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)

svm = SGDClassifier(loss='hinge')
svm.fit(x_train_std, y_train)
logistic_regression = SGDClassifier(loss='log')
logistic_regression.fit(x_train_std, y_train)
ppn = SGDClassifier(loss='perceptron')
ppn.fit(x_train_std, y_train)

y_pred = svm.predict(x_test_std)

print('Misclassified samples: %d' % (y_test != y_pred).sum())

print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))

x_combined_std = np.vstack((x_train_std, x_test_std))
y_combined_std = np.hstack((y_train, y_test))
plot_decision_regions(
    x_combined_std, y_combined_std, classifier=ppn, test_idx=range(105, 150))

x_combined_std = np.vstack((x_train_std, x_test_std))
y_combined_std = np.hstack((y_train, y_test))
plot_decision_regions(
    x_combined_std, y_combined_std,
    classifier=logistic_regression, test_idx=range(105, 150))

x_combined_std = np.vstack((x_train_std, x_test_std))
y_combined_std = np.hstack((y_train, y_test))
plot_decision_regions(
    x_combined_std, y_combined_std,
    classifier=svm, test_idx=range(105, 150))
