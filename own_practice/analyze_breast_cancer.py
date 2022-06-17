"""Analyz."""

import numpy as np
from plot_decision_regions import plot_decision_regions
from plot_decision_regions import learn_module
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

MODELS = ['perceptron', 'log', 'svm', 'rbf', 'knn']

x_data = load_breast_cancer().data
y_data = load_breast_cancer().target
class_names = load_breast_cancer().target_names

classes, class_num = np.unique(y_data, return_counts=True)

for value in range(31):
    x_data = PCA(n_components=2).fit_transform(x_data)
    x_data = StandardScaler().fit_transform(x_data)

    x_train, x_test, y_train, y_test = train_test_split(
        x_data, y_data, test_size=0.2, random_state=0)

    sc = StandardScaler()
    sc.fit(x_train)
    x_train_std = sc.transform(x_train)
    x_test_std = sc.transform(x_test)

    for model_name in MODELS:
        model = learn_module(x_train_std, y_train, model_name=model_name)

        y_pred = model.predict(x_test_std)
        print('Misclassified samples: %d' % (y_test != y_pred).sum())

        print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))

        x_combined_std = np.vstack((x_train_std, x_test_std))
        y_combined_std = np.hstack((y_train, y_test))

        plot_decision_regions(
            x_combined_std, y_combined_std, model_name=model_name,
            classifier=model, test_idx=range(105, 150))
