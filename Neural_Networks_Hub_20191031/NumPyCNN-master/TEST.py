import skimage.data
import numpy
import NumPyCNN as numpycnn

print("###### ###### ###### ###### ###### ###### 1.读取输入图像 ###### ###### ###### ###### ###### ######")
# Reading the image
img = skimage.data.chelsea()
print("img:",img.shape,"\n",img)
# Converting the image into gray.
img = skimage.color.rgb2gray(img)
print("img:",img.shape,"\n",img)

print("###### ###### ###### ###### ###### ###### 2.准备滤波器 ###### ###### ###### ###### ###### ######")
l1_filter = numpy.zeros((2,3,3))
l1_filter[0, :, :] = numpy.array([[[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]]])
l1_filter[1, :, :] = numpy.array([[[1,  1, 1],[0,  0, 0],[-1, -1, -1]]])
print("l1_filter:",l1_filter.shape,"\n",l1_filter)

print("###### ###### ###### ###### ###### ###### 3.卷积层（Conv Layer） ###### ###### ###### ###### ###### ######")
l1_feature_map = numpycnn.conv(img, l1_filter)
print("l1_feature_map:",l1_feature_map.shape,"\n",l1_feature_map)

print("###### ###### ###### ###### ###### ###### 4.ReLU激活函数层 ###### ###### ###### ###### ###### ######")
l1_feature_map_relu = numpycnn.relu(l1_feature_map)
print("l1_feature_map_relu:",l1_feature_map_relu.shape,"\n",l1_feature_map_relu)

print("###### ###### ###### ###### ###### ###### 5.最大池化层 ###### ###### ###### ###### ###### ######")
l1_feature_map_relu_pool = numpycnn.pooling(l1_feature_map_relu, 2, 2)
print("l1_feature_map_relu_pool:",l1_feature_map_relu_pool.shape,l1_feature_map_relu_pool.shape[-1],"\n",l1_feature_map_relu_pool)

# print("###### ###### ###### ###### ###### ###### 6.层堆叠 ###### ###### ###### ###### ###### ######")

