# 01$.@victorczhou-CNN 02$.@victorczhou-MLP 03$.@aliyun-CNN 04$.@白手起家的百万富翁-MLP 05$.@<<Tensorflow 实战>>
"""
import mnist

train_images = mnist.train_images()[:1000]
train_labels = mnist.train_labels()[:1000]
print(train_images)
print(type(train_images),train_images.shape)
print(train_labels)
print(type(train_labels),train_labels.shape)

test_images = mnist.test_images()[:1000]
test_labels = mnist.test_labels()[:1000]
"""
"""
import numpy as np

# train_images = np.array([[[1,2,3], [4,5,6], [7,8,9]],[[10,20,30], [40,50,60], [70,80,90]],[[100,200,300], [400,500,600], [700,800,900]]])
train_images = np.array([[[1,2,3], [4,5,6], [7,8,9]],[[10,20,30], [40,50,60], [70,80,90]]])
train_labels = np.array([11,12,13])
print(train_images)
print(type(train_images),train_images.shape)
print(train_labels)
print(type(train_labels),train_labels.shape)
print("-----------------------------------")

for i, (im, label) in enumerate(zip(train_images, train_labels)):
    print("i:=",type(i),i)
    print("im:=",type(im),im)
    print("label:=",type(label),label)
"""

import mnist
from conv import Conv3x3
from maxpool import MaxPool2
from softmax import Softmax

conv = Conv3x3(8)                  # 28x28x1 -> 26x26x8
pool = MaxPool2()                  # 26x26x8 -> 13x13x8
softmax = Softmax(13 * 13 * 8, 10) # 13x13x8 -> 10

print("###### ###### ###### ###### ###### ###### 01$.train_image[0] ###### ###### ###### ###### ###### ######")
image = mnist.train_images()[0]
image = (image / 255) - 0.5
print(image)
print(image.shape)

print("###### ###### ###### ###### ###### ###### 02$.out_conv ###### ###### ###### ###### ###### ######")
print("conv.filters:=",conv.filters)
print("conv.filters.shape:=",conv.filters.shape)
out = conv.forward(image)
print(out)
print(out.shape)
print("###### ###### ###### ###### ###### ###### 03$.out_pool ###### ###### ###### ###### ###### ######")
out = pool.forward(out)
print(out)
print(out.shape)
print("###### ###### ###### ###### ###### ###### 04$.out_softmax ###### ###### ###### ###### ###### ######")
print("Softmax(input_len:=13 * 13 * 8, nodes:=10)")
out = softmax.forward(out)
print(out)
print(out.shape)