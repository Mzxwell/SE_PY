from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from ucimlrepo import fetch_ucirepo
# fetch dataset
adult = fetch_ucirepo(id=2)
# data (as pandas dataframes)
X = adult.data.features
y = adult.data.targets.values.ravel()  # 使用 ravel() 确保 y 为一维数组
# 预处理数据
# 将目标变量 (income) 转换为数值
y = LabelEncoder().fit_transform(y)
categorical_columns = X.select_dtypes(include=['object']).columns.tolist()
# 将分类特征转换为数值 (如果有必要)
# 假设 X 已经是 DataFrame 格式，且需要编码的列为 'workclass', 'marital-status', 'occupation', 'relationship', 'race', 'sex'
for col in categorical_columns:
    le = LabelEncoder()
    X.loc[:, col] = le.fit_transform(X[col])

# 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建决策树分类器
clf = DecisionTreeClassifier(criterion='gini', splitter='best')

# 训练模型
clf.fit(x_train, y_train)

# 测试模型
accuracy = clf.score(x_test, y_test)
print(f"Test Accuracy: {accuracy:.4f}")
fig=plt.figure(figsize=(655,655))
_=plot_tree(
    clf,
    feature_names=adult.feature_names,
    class_names=adult.target_names,
    filled=True,
)
fig.savefig('decision_tree.png')