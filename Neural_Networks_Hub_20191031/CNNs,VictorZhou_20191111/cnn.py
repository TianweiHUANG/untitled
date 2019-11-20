import mnist # - ok
import numpy as np # - ok
from conv import Conv3x3 # - ok
from maxpool import MaxPool2 # - ok
from softmax import Softmax # - ok

# We only use the first 1k examples of each set in the interest of time. # - ok
# Feel free to change this if you want. # - ok
train_images = mnist.train_images()[:1000] # - ok
train_labels = mnist.train_labels()[:1000] # - ok
test_images = mnist.test_images()[:1000] # - ok
test_labels = mnist.test_labels()[:1000] # - ok

conv = Conv3x3(8) # - ok                  # 28x28x1 -> 26x26x8
pool = MaxPool2() # - ok                  # 26x26x8 -> 13x13x8
softmax = Softmax(13 * 13 * 8, 10) # - ok # 13x13x8 -> 10

def forward(image, label):
  '''
  Completes a forward pass of the CNN and calculates the accuracy and
  cross-entropy loss.
  - image is a 2d numpy array
  - label is a digit
  '''
  # We transform the image from [0, 255] to [-0.5, 0.5] to make it easier
  # to work with. This is standard practice.
  out = conv.forward((image / 255) - 0.5)
  out = pool.forward(out)
  out = softmax.forward(out)

  # Calculate cross-entropy loss and accuracy. np.log() is the natural log.
  loss = -np.log(out[label])
  acc = 1 if np.argmax(out) == label else 0

  return out, loss, acc

def train(im, label, lr=.005):
  '''
  Completes a full training step on the given image and label.
  Returns the cross-entropy loss and accuracy.
  - image is a 2d numpy array
  - label is a digit
  - lr is the learning rate
  '''
  # Forward
  out, loss, acc = forward(im, label)

  # Calculate initial gradient
  gradient = np.zeros(10)
  gradient[label] = -1 / out[label]

  # Backprop
  gradient = softmax.backprop(gradient, lr)
  gradient = pool.backprop(gradient)
  gradient = conv.backprop(gradient, lr)

  return loss, acc

print('MNIST CNN initialized!') # - ok

# Train the CNN for 3 epochs # - ok
for epoch in range(3): # - ok
  print('--- Epoch %d ---' % (epoch + 1)) # - ok

  # Shuffle the training data # - ok
  permutation = np.random.permutation(len(train_images)) # - ok
  train_images = train_images[permutation] # - ok
  train_labels = train_labels[permutation] # - ok

  # Train! # - ok
  loss = 0 # - ok
  num_correct = 0 # - ok
  # Ng # Ng # Ng # Ng # Ng # Ng
  for i, (im, label) in enumerate(zip(train_images, train_labels)):
    if i % 100 == 99:
      print(
        '[Step %d] Past 100 steps: Average Loss %.3f | Accuracy: %d%%' %
        (i + 1, loss / 100, num_correct)
      )
      loss = 0
      num_correct = 0

    l, acc = train(im, label)
    loss += l
    num_correct += acc
  # Ng # Ng # Ng # Ng # Ng # Ng

# Test the CNN # - ok
print('\n--- Testing the CNN ---') # - ok
loss = 0 # - ok
num_correct = 0 # - ok
for im, label in zip(test_images, test_labels): # - ok
  _, l, acc = forward(im, label) # Ng # Ng # Ng # Ng # Ng # Ng
  loss += l # - ok
  num_correct += acc # - ok

num_tests = len(test_images) # - ok
print('Test Loss:', loss / num_tests) # - ok
print('Test Accuracy:', num_correct / num_tests) # - ok
