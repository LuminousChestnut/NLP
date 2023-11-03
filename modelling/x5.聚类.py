# 聚类是一种无监督学习算法，用于将数据集中的对象分成几个相似的组或类别。聚类算法的目标是找到一些相似的数据点，并将它们分成不同的类别或簇，使得同一类别的数据点尽可能地相似，而不同类别的数据点尽可能地不同。
#
# 常见的聚类算法包括 K-Means 算法、层次聚类算法和 DBSCAN 算法等。
# 其中，K-Means 算法是最常见的聚类算法之一，它将数据点分为 K 个簇，并将每个数据点分配到最近的簇中，

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

# 生成模拟数据
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# 创建 KMeans 聚类器并拟合数据
kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(X)

# 预测数据的簇标签
y_pred = kmeans.predict(X)

# 绘制聚类结果
plt.scatter(X[:, 0], X[:, 1], c=y_pred, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
