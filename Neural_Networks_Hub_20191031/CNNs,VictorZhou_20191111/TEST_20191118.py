# 01$.@ victorczhou-CNN
# 02$.@ victorczhou-MLP
# 03$.@ aliyun-CNN
# 04$.@ 白手起家的百万富翁-MLP
# 05$.@ <<Tensorflow 实战>>
# -正态分布/ -softmax/ -交叉熵/

import mnist
import numpy as np

# train_images = mnist.train_images()[:1000]# <class 'numpy.ndarray'> (1000, 28, 28)
# train_labels = mnist.train_labels()[:1000]# <class 'numpy.ndarray'> (1000,)
train_images = np.array([[[1,2,3,4], [5,6,7,8], [9,10,11,12]],[[10,20,30,40], [50,60,70,80], [90,100,110,120]]])
train_labels = np.array([1000,2000])
print(train_images)
print(type(train_images),train_images.shape)
print(train_labels)
print(type(train_labels),train_labels.shape)

for i, (im, label) in enumerate(zip(train_images, train_labels)):
    print("------ ------ ------")
    print("i:=",type(i),i)
    print("im:=",type(im),im)
    print("label:=",type(label),label)

"""
import mnist
import numpy as np
from conv import Conv3x3
from maxpool import MaxPool2
from softmax import Softmax
print("######-######-######-######-######-###### 1/5 $.train_image[0] ######-######-######-######-######-######")
image = mnist.train_images()[0]
print(image.shape,"\n",image)
image = (image / 255) - 0.5
print(image.shape,"\n",image)
print("######-######-######-######-######-###### 2/5 $.out_conv ######-######-######-######-######-######")
conv = Conv3x3(8)                  # 28x28x1 -> 26x26x8
print("filters.shape:=",conv.filters.shape,"\n","filters:=",conv.filters)
out = conv.forward(image)
print(out.shape,"\n",out)
print("######-######-######-######-######-###### 3/5 $.out_pool ######-######-######-######-######-######")
pool = MaxPool2()                  # 26x26x8 -> 13x13x8
out = pool.forward(out)
print(out.shape,"\n",out)
print("######-######-######-######-######-###### 4/5 $.out_softmax ######-######-######-######-######-######")
softmax = Softmax(13 * 13 * 8, 10) # 13x13x8 -> 10
print("softmax(input_len:=13 * 13 * 8, nodes:=10)")
out = softmax.forward(out)
print(out.shape,"\n",out)
print("######-######-######-######-######-###### 5/5 $.loss,acc ######-######-######-######-######-######")
# Calculate cross-entropy loss and accuracy. np.log() is the natural log.
label = mnist.train_labels()[0]
loss = -np.log(out[label])
acc = 1 if np.argmax(out) == label else 0
print("label:=",label,"label.shape:=",label.shape,"acc:=",acc,"loss:=",loss)
"""