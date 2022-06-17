"""Support Vector Machine kernel trick.

使用scilit-learn實作Support Vector Machine演算法，使用核技巧。
"""
import matplotlib.pyplot as plt
import numpy as np
from plot_decision_regions import plot_decision_regions
from sklearn.svm import SVC

np.random.seed(0)
x_xor = np.random.randn(200, 2)
y_xor = np.logical_xor(x_xor[:, 0] > 0, x_xor[:, 1] > 0)
y_xor = np.where(y_xor, 1, -1)

plt.scatter(
    x_xor[y_xor == 1, 0], x_xor[y_xor == 1, 1], c='b', marker='x', label='1')
plt.scatter(
    x_xor[y_xor == -1, 0], x_xor[y_xor == -1, 1], c='r', marker='s', label='-1'
    )

plt.ylim(-3.0)
plt.legend('')
plt.show()

svm = SVC(kernel='rbf', C=10.0, random_state=0, gamma=0.10)
svm.fit(x_xor, y_xor)

plot_decision_regions(x_xor, y_xor, classifier=svm)
