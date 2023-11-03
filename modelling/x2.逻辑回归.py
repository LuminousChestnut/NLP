# 逻辑回归是一种常见的分类算法，用于将一个或多个自变量与一个二元或多元离散的因变量之间的关系建模。它的名字"逻辑"来源于它的模型本质上是一个逻辑函数，用于将输入值转换为一个概率值。逻辑回归通常用于二元分类问题，但也可以扩展到多元分类问题。
#
# 逻辑回归模型的基本形式如下：
#
# p（y=1|x） = 1 / （1 + exp（-（b0 + b1x1 + b2x2 + ... + bpxp）））
#
# 其中，p（y=1|x） 是给定自变量 x 下因变量 y 取值为 1 的概率，exp（） 是指数函数，b0， b1， b2， ...， bp 是模型的系数。
#
# 逻辑回归的目标是找到最优的系数 b0， b1， b2， ...， bp，以最大化似然函数，从而使模型预测的结果尽可能地接近真实值。通常，我们会使用极大似然估计法来估计模型的系数。
#
# 在训练过程中，逻辑回归模型使用一个称为逻辑损失函数的代价函数来衡量预测结果与真实值之间的误差。逻辑损失函数如下：
#
# J（b） = （-1/m） * Σ[yi*log（p（xi）） + （1-yi）*log（1-p（xi））]
#
# 其中，m 是样本数量，yi 是真实的分类标签（0 或 1），p（xi） 是模型预测的分类概率。
#
# 逻辑回归可以使用梯度下降法或牛顿法等优化算法来最小化逻辑损失函数，从而得到最优的模型参数。最后，模型将自变量输入到逻辑函数中，得到分类概率，并使用阈值将概率转化为分类标签，通常取阈值为 0.5。
#
# 逻辑回归在实际中的应用非常广泛，比如在金融、医学、社会科学等领域中，都可以使用逻辑回归来预测和分析数据。
#
# 下面是一个简单的 Python 代码实现逻辑回归：

# 这个代码使用了 Numpy 库生成了一个包含 100 个样本的随机数据集，并使用 Scikit-learn 库的 LogisticRegression 类创建了一个逻辑回归模型。
# 模型通过 fit（） 方法拟合数据，并通过 predict（） 方法预测测试集的结果。
# 最后，代码使用 accuracy_score（） 方法计算模型的准确率，并打印出结果。

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 创建一个随机数据集
for _ in range(100):
    np.random.seed(_)
    X = np.random.rand(100, 3)
    y = np.random.randint(0, 2, 100)

    # 划分数据集为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # 创建逻辑回归模型并拟合数据
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # 预测测试集的结果
    y_pred = model.predict(X_test)

    # 计算准确率
    accuracy = accuracy_score(y_test, y_pred)
    # print('Accuracy:', accuracy)
    accuracyList = [accuracy]
