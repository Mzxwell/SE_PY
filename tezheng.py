# coding=utf-8
# 读取数据集，这里以CIFAR-10为例，可以加载自己的图片
# 文件的读取，直接通过给定的`load_CIFAR10`模块读取数据。
import load_data
from load_data import load_CIFAR10
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image
from skimage import feature as ft

# cifar10_dir = '/Users/mac/Downloads/cifar-10-batches-py'


# 读取文件，并把数据保存到训练集和测试集合。
X_train, y_train, X_test, y_test = load_data.get_train_data()

# 先来查看一下每个变量的大小，确保没有任何错误！X_train和X_test的大小应该为 N*W*H*3
# N: 样本个数, W: 样本宽度 H: 样本高度， 3: RGB颜色。 y_train和y_test为图片的标签。
print ("训练数据和测试数据:", X_train.shape, y_train.shape, X_test.shape, y_test.shape)
print ("标签的种类: ", np.unique(y_train))  # 查看标签的个数以及标签种类，预计10个类别。

classes = ['01', '02', '03']
num_classes = len(classes)  # 样本种类的个数
# samples_per_class = 5  # 每一个类随机选择5个样本

# plt.subplot函数以及 plt.imshow函数用来展示图片

# for y, cls in enumerate(classes):
#     idxs = np.flatnonzero(y_train == y)
#     idxs = np.random.choice(idxs, samples_per_class, replace=False)
#     for i, idx in enumerate(idxs):
#         plt_idx = i * num_classes + y + 1
#         plt.subplot(samples_per_class, num_classes, plt_idx)
#         plt.imshow(X_train[idx].astype('uint8'))
#         plt.axis('off')
#         if i == 0:
#             plt.title(cls)
# plt.show()

# number_of_each_class = []
# for y, cls in enumerate(classes):
#     idxs = np.flatnonzero(y_train == y)
#     number_of_each_class.append(len(idxs))
# plt.plot(classes, number_of_each_class)
# plt.show()

# 随机采样训练样本5000个和测试样本500个。训练样本从训练集里采样，测试样本从测试集里采样。
# num_training = 5000
# num_test = 500
#
# random_train = np.random.randint(50000, size=5000)
# random_test = np.random.randint(10000, size=500)
#
# X_train = X_train[random_train]
# y_train = y_train[random_train]

# X_test = X_test[random_test]
# y_test = y_test[random_test]

# print (X_train.shape, y_train.shape, X_test.shape, y_test.shape)

# 首先我们 Reshape一下图片。图片是的每一个图片变成一个向量的形式。也就是把原来大小为(32, 32, 3)的图片直接转换成一个长度为32*32*3=3072的向量。
# 这样就直接可以作为模型的输入。 X_train_1和y_train_1是用来解决第一个问题的处理后的数据。
X_train1 = np.reshape(X_train, (X_train.shape[0], -1))
X_tes