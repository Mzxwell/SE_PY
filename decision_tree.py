import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree

# 加载 Iris 数据集
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

# 数据清洗
# 但为了保持通用性，假设需要处理缺失值，使用均值填充
X.fillna(X.mean(), inplace=True)  # 用均值填充缺失值

# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)
clf = DecisionTreeClassifier( min_samples_split=5# 剪枝
                              ,criterion='gini', splitter='best')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
score = accuracy_score(y_test, y_pred)
print("准确率：", score)
fig = plt.figure(figsize=(25, 20))
_ = plot_tree(
    clf,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
)
fig.savefig('决策树.png')
