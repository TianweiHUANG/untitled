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
