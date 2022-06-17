"""Decision regions diagram."""

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

MARKERS = ('s', 'x', 'o', '^', 'v')
COLORS = ('red', 'blue', 'lightgreen', 'gray', 'cyan')


def plot_decision_regions(
        x_data, y_data, classifier, model_name='decision_regions_diagram',
        test_idx=None, resolution=0.02):
    """Decision regions diagram."""
    # setup marker generator and color map
    cmap = ListedColormap(COLORS[:len(np.unique(y_data))])
    x1_min, x1_max = x_data[:, 0].min() - 1, x_data[:, 0].max() + 1
    x2_min, x2_max = x_data[:, 1].min() - 1, x_data[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(
        np.arange(x1_min, x1_max, resolution),
        np.arange(x2_min, x2_max, resolution))
    z_data = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    z_data = z_data.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z_data, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    x_test, _ = x_data[test_idx, :], y_data[test_idx]
    for idx, c_l in enumerate(np.unique(y_data)):
        plt.scatter(
            x=x_data[y_data == c_l, 0], y=x_data[y_data == c_l, 1],
            alpha=0.8, c=cmap(idx), marker=MARKERS[idx], label=c_l)

    if test_idx:
        x_test, _ = x_data[test_idx, :], y_data[test_idx]
        plt.scatter(
            x_test[:, 0], x_test[:, 1], alpha=1.0, linewidth=1,
            marker='o', s=55, label='test set')

    plt.xlabel('petal length [standardized]')
    plt.ylabel('petal width [standardized]')
    plt.savefig(model_name + '.png')
    # plt.show()
    plt.close()


def learn_module(x_train_std, y_train, model_name=None):
    """自動回傳與選擇訓練模型."""
    if model_name == 'perceptron':
        model = Perceptron(max_iter=1000, eta0=0.1, random_state=0)
        model.fit(x_train_std, y_train)

    elif model_name == 'log':
        model = LogisticRegression(C=1000.0, random_state=0)
        model.fit(x_train_std, y_train)

    elif model_name == 'svm':
        model = SVC(kernel='linear', C=1.0, random_state=0)
        model.fit(x_train_std, y_train)

    elif model_name == 'rbf':
        model = SVC(kernel='rbf', C=1.0, gamma=1.0, random_state=0)
        model.fit(x_train_std, y_train)

    elif model_name == 'knn':
        n_neighbors = 5   # 選擇 K 值
        weights = 'uniform'  # 選擇權重：'uniform' 或 'distance'
        model = KNeighborsClassifier(n_neighbors=n_neighbors, weights=weights)
        model.fit(x_train_std, y_train)

    elif model_name == 'tree':
        model = DecisionTreeClassifier(max_depth=2)
        model.fit(x_train_std, y_train)

    elif model_name == 'random_forest':
        model = RandomForestClassifier(
            criterion='entropy',
            n_estimators=10,
            random_state=1,
            n_jobs=2
            )
        model.fit(x_train_std, y_train)

    else:
        print("Have not model!")
        model = None

    return model
