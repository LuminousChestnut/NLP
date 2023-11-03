# 支持向量机（Support Vector Machine，简称 SVM）是一种常用的监督学习算法，常用于分类和回归问题。SVM 基于将数据映射到高维空间，并在该空间中寻找最大间隔超平面来进行分类或回归。
#
# SVM 的目标是找到一个最大间隔超平面，它将不同类别的数据分开，使得同一类别的数据点尽可能地靠近这个超平面。具体来说，对于二分类问题，SVM 将数据映射到高维空间，并找到一个超平面，它能够将两类数据分开，并且距离两类数据点最近的点到该超平面的距离最大。
#
# 在实现 SVM 时，需要选择一个核函数来对数据进行映射，常用的核函数有线性核、多项式核和径向基函数（Radial Basis Function，简称 RBF）核等。
#
# 下面是一个使用 Scikit-learn 库中的 SVM 类（SVC）实现分类问题的示例代码：

from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# 载入数据集
iris = load_iris()

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# 创建 SVM 分类器并拟合数据
clf = SVC(kernel='linear', C=1.0, random_state=42)
clf.fit(X_train, y_train)

# 预测测试集的结果
y_pred = clf.predict(X_test)

# 计算分类器在测试集上的准确率
accuracy = clf.score(X_test, y_test)
print("Accuracy: {:.2f}%".format(accuracy * 100))