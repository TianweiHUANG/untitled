import numpy as np
import mnist
#from conv import Conv3x3

class Conv3x3:
  # A Convolution layer using 3x3 filters.

  def __init__(self, num_filters):
    self.num_filters = num_filters

    # filters is a 3d array with dimensions (num_filters, 3, 3)
    # We divide by 9 to reduce the variance of our initial values
    self.filters = np.random.randn(num_filters, 3, 3) / 9

  def iterate_regions(self, image):
    '''
    Generates all possible 3x3 image regions using valid padding.
    - image is a 2d numpy array
    '''
    h, w = image.shape

    for i in range(h - 2):
      for j in range(w - 2):
        im_region = image[i:(i + 3), j:(j + 3)]
        yield im_region, i, j

  def forward(self, input):
    '''
    Performs a forward pass of the conv layer using the given input.
    Returns a 3d numpy array with dimensions (h, w, num_filters).
    - input is a 2d numpy array
    '''
    h, w = input.shape
    output = np.zeros((h - 2, w - 2, self.num_filters))

    for im_region, i, j in self.iterate_regions(input):
      output[i, j] = np.sum(im_region * self.filters, axis=(1, 2))

    return output

# The mnist package handles the MNIST dataset for us!
# Learn more at https://github.com/datapythonista/mnist
train_images = mnist.train_images()
train_labels = mnist.train_labels()
print(train_images[0])
print(train_labels[0])

conv = Conv3x3(8)
output = conv.forward(train_images[0])
print(output.shape) # (26, 26, 8)
# http://scs.ryerson.ca/~aharley/vis/conv/
# 01$.@victorczhou-CNN 02$.@victorczhou-MLP 03$.@aliyun-CNN 04$.@白手起家的百万富翁-MLP 05$.@<<Tensorflow 实战>>
"""
import skimage.data
import matplotlib
import matplotlib.pyplot as plt
import numpy

img = skimage.data.chelsea()
matplotlib.image.imsave('Neural_Network_img.png', img)
plt.imshow(img)
plt.savefig("Neural_Network_img_plt.png")
print(img)

img = skimage.color.rgb2gray(img)
matplotlib.image.imsave('Neural_Network_img_gray.png', img)
plt.imshow(img)
plt.savefig("Neural_Network_img_gray_plt.png")
print(img)

l1_filter = numpy.zeros((2,3,3))
print(l1_filter)
l1_filter[0, :, :] = numpy.array([[[-1, 0, 1], [-1, 0, 1],[-1, 0, 1]]])
l1_filter[1, :, :] = numpy.array([[[1,   1,  1], [0,   0,  0],[-1, -1, -1]]])
print(l1_filter)
"""