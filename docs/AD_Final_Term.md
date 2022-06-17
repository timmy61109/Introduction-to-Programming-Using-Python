# 資料集分割及訓練方式
`analyze_breast_cancer.py` 主要程式碼。

```python
"""Analyz breast cancer."""

import numpy as np
from plot_decision_regions import learn_module
from plot_decision_regions import plot_decision_regions
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

MODELS = ['perceptron', 'log', 'svm', 'rbf', 'knn', 'tree', 'random_forest']


for value in range(30):
    for value_2 in range(30):
        if value != value_2:
            x_data = load_breast_cancer().data[:, [value, value_2]]
            y_data = load_breast_cancer().target
            class_names = load_breast_cancer().target_names
            classes, class_num = np.unique(y_data, return_counts=True)

            x_train, x_test, y_train, y_test = train_test_split(
                x_data, y_data, test_size=0.2, random_state=0)

            sc = StandardScaler()
            sc.fit(x_train)
            x_train_std = sc.transform(x_train)
            x_test_std = sc.transform(x_test)

            for model_name in MODELS:
                model = learn_module(
                    x_train_std, y_train, model_name=model_name)

                y_pred = model.predict(x_test_std)
                print('Misclassified samples: %d' % (y_test != y_pred).sum())

                print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))

                if accuracy_score(y_test, y_pred) >= 0.97:
                    x_combined_std = np.vstack((x_train_std, x_test_std))
                    y_combined_std = np.hstack((y_train, y_test))

                    plot_decision_regions(
                        x_combined_std, y_combined_std,
                        model_name=model_name + "_" + str(value) +
                        'x' + str(value + 1) +
                        "_" + str(accuracy_score(y_test, y_pred)),
                        classifier=model, test_idx=range(105, 150))
```

`plot_decision_regions.py` 繪製圖表與演算法選擇模組與函式。

```python
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
```

# 計算分類指標

1. Accuracy
2. Precision
3. Recall
4. F1 score
5. Sensitivity
6. Specificity
7. ROC AUC

礙於自己這學期才轉學進來，基礎知識不足，花了很多時間在學習Python跟趕進度，因此目前只有找到Accuracy的數據輸出方法。

# 至少有一種方法精確率(Accuracy)要達到0.97
目前實際測試達到 $97\%$ ，有以下是可以到達的演算法產生的決策區域圖。

## 決策樹

Row 3 and Row 4: 0.9736842105263158

![](assets/AD_Final_Term-8478bea9.png)

Row 27 and Row 28: 0.9736842105263158

![](assets/AD_Final_Term-08a588bd.png)

## RBF SVM

Row 22 and Row 23: 0.9736842105263158

![](assets/AD_Final_Term-a97f9f22.png)

Row 24 and Row 25: 0.9736842105263158

![](assets/AD_Final_Term-b66696d0.png)

## Perceptron

Row 22 and Row 23: 0.9736842105263158

![](assets/AD_Final_Term-b164e5d4.png)

Row 24 and Row 25: 0.9736842105263158

![](assets/AD_Final_Term-1eba6c08.png)

# 參考資料
- [3.1. Cross-validation: evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html)
- [[Day29]機器學習：交叉驗證！](https://ithelp.ithome.com.tw/articles/10197461)
- [sklearn.linear_model.Perceptron](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html)
- [Perceptron in Python](https://stackoverflow.com/questions/62317094/perceptron-in-python)
- [從圖表秒懂機器學習模型的原理：以 matplotlib 視覺化 scikit-learn 的分類器（KNN、邏輯斯迴歸、SVM、決策樹、隨機森林）](https://alankrantas.medium.com/%E7%94%A8%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92%E6%A8%A1%E5%9E%8B%E7%94%A2%E7%94%9F%E5%9C%96%E8%A1%A8-%E7%A7%92%E6%87%82%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92%E7%9A%84%E5%8E%9F%E7%90%86-%E4%BB%A5-matplotlib-%E8%A6%96%E8%A6%BA%E5%8C%96-scikit-learn-%E7%9A%84%E5%88%86%E9%A1%9E%E5%99%A8-knn-%E9%82%8F%E8%BC%AF%E6%96%AF%E8%BF%B4%E6%AD%B8-svm-%E6%B1%BA%E7%AD%96%E6%A8%B9-%E9%9A%A8%E6%A9%9F%E6%A3%AE%E6%9E%97-2f01aec48b54)
- [What is PEP8's E128: continuation line under-indented for visual indent?](https://stackoverflow.com/questions/15435811/what-is-pep8s-e128-continuation-line-under-indented-for-visual-indent)
- [ValueError: 'c' argument must be a color, a sequence of colors, or a sequence of numbers](https://stackoverflow.com/questions/71653179/valueerror-c-argument-must-be-a-color-a-sequence-of-colors-or-a-sequence-of)
- [[Solved] ValueError: 'c' argument must be a color, a sequence of colors, or a sequence of numbers](https://solveforum.com/forums/threads/solved-valueerror-c-argument-must-be-a-color-a-sequence-of-colors-or-a-sequence-of-numbers.740918/)
- [Scatter plot with non-sequence ´c´ color should give a better Error message.](https://github.com/matplotlib/matplotlib/issues/10365/)
- [Pylint: How to fix "c0209: formatting a regular string which could be a f-string (consider-using-f-string)"](https://miguendes.me/pylint-consider-using-f-string)
- ROC/AUC
  - [淺談機器學習的效能衡量指標 (2) -- ROC/AUC 曲線](https://ithelp.ithome.com.tw/articles/10229049)
  - [AI_Applications](https://github.com/mc6666/AI_Applications)
  - [深入介紹及比較ROC曲線及PR曲線](https://medium.com/nlp-tsupei/roc-pr-%E6%9B%B2%E7%B7%9A-f3faa2231b8c)
- `.data`
  - [快速解析 Python 的各種 Import Data 基礎應用技巧](https://chriskang028.medium.com/datacamp-importing-data-in-python-%E8%AA%B2%E7%A8%8B%E7%AD%86%E8%A8%98-50141c6777b)
