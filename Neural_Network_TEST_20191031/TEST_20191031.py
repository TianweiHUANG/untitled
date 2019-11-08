# http://scs.ryerson.ca/~aharley/vis/conv/
# 01$.@victorczhou-CNN 02$.@victorczhou-MLP 03$.@aliyun-CNN 04$.@白手起家的百万富翁-MLP 05$.@<<Tensorflow 实战>>

import mnist
#-
train_images = mnist.train_images()[0]
train_labels = mnist.train_labels()[0]
print(train_images)
print(train_images.shape)
print(train_labels)
print(train_labels.shape)
train_images = mnist.train_images()[:1000]
train_labels = mnist.train_labels()[:1000]
#-
test_images = mnist.test_images()[0]
test_labels = mnist.test_labels()[0]
print(test_images)
print(test_images.shape)
print(test_labels)
print(test_labels.shape)
test_images = mnist.test_images()[:1000]
test_labels = mnist.test_labels()[:1000]