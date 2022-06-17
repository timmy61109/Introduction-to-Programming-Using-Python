"""Decision regions diagram."""

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np

MARKERS = ('s', 'x', 'o', '^', 'v')
COLORS = ('red', 'blue', 'lightgreen', 'gray', 'cyan')


def plot_decision_regions(
        x_data, y_data, classifier, test_idx=None, resolution=0.02):
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
    plt.show()
