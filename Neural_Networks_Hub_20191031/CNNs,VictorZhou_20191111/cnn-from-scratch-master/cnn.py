import mnist
import numpy as np
from conv import Conv3x3
from maxpool import MaxPool2
from softmax import Softmax

# We only use the first 1k examples of each set in the interest of time.
# Feel free to change this if you want.
train_images = mnist.train_images()[:1000]
train_labels = mnist.train_labels()[:1000]
test_images = mnist.test_images()[:1000]
test_labels = mnist.test_labels()[:1000]

conv = Conv3x3(8)                  # 28x28x1 -> 26x26x8
pool = MaxPool2()                  # 26x26x8 -> 13x13x8
softmax = Softmax(13 * 13 * 8, 10) # 13x13x8 -> 10

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

print('MNIST CNN initialized!')

# Train the CNN for 3 epochs
for epoch in range(3):
  print('--- Epoch %d ---' % (epoch + 1))

  # Shuffle the training data
  permutation = np.random.permutation(len(train_images))
  train_images = train_images[permutation]
  train_labels = train_labels[permutation]

  # Train!
  loss = 0
  num_correct = 0
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

# Test the CNN
print('\n--- Testing the CNN ---')
loss = 0
num_correct = 0
for im, label in zip(test_images, test_labels):
  _, l, acc = forward(im, label)
  loss += l
  num_correct += acc

num_tests = len(test_images)
print('Test Loss:', loss / num_tests)
print('Test Accuracy:', num_correct / num_tests)

# "F:\Program Files (x86)\Python37\python.exe" F:/TianweiHUANG_BGI_Backups_20180504_附件/Python_Practise_20190604/
#    PycharmProjects/untitled/Neural_Networks_Hub_20191031/CNNs,VictorZhou_20191111/cnn-from-scratch-master/cnn.py
# MNIST CNN initialized!
# --- Epoch 1 ---
# [Step 100] Past 100 steps: Average Loss 2.192 | Accuracy: 22%
# [Step 200] Past 100 steps: Average Loss 1.993 | Accuracy: 33%
# [Step 300] Past 100 steps: Average Loss 1.577 | Accuracy: 56%
# [Step 400] Past 100 steps: Average Loss 1.045 | Accuracy: 66%
# [Step 500] Past 100 steps: Average Loss 1.056 | Accuracy: 67%
# [Step 600] Past 100 steps: Average Loss 0.777 | Accuracy: 76%
# [Step 700] Past 100 steps: Average Loss 0.816 | Accuracy: 75%
# [Step 800] Past 100 steps: Average Loss 0.727 | Accuracy: 79%
# [Step 900] Past 100 steps: Average Loss 0.688 | Accuracy: 79%
# [Step 1000] Past 100 steps: Average Loss 0.629 | Accuracy: 82%
# --- Epoch 2 ---
# [Step 100] Past 100 steps: Average Loss 0.666 | Accuracy: 82%
# [Step 200] Past 100 steps: Average Loss 0.534 | Accuracy: 83%
# [Step 300] Past 100 steps: Average Loss 0.526 | Accuracy: 81%
# [Step 400] Past 100 steps: Average Loss 0.645 | Accuracy: 82%
# [Step 500] Past 100 steps: Average Loss 0.644 | Accuracy: 80%
# [Step 600] Past 100 steps: Average Loss 0.364 | Accuracy: 88%
# [Step 700] Past 100 steps: Average Loss 0.458 | Accuracy: 86%
# [Step 800] Past 100 steps: Average Loss 0.525 | Accuracy: 84%
# [Step 900] Past 100 steps: Average Loss 0.587 | Accuracy: 81%
# [Step 1000] Past 100 steps: Average Loss 0.339 | Accuracy: 88%
# --- Epoch 3 ---
# [Step 100] Past 100 steps: Average Loss 0.354 | Accuracy: 88%
# [Step 200] Past 100 steps: Average Loss 0.409 | Accuracy: 90%
# [Step 300] Past 100 steps: Average Loss 0.455 | Accuracy: 87%
# [Step 400] Past 100 steps: Average Loss 0.339 | Accuracy: 92%
# [Step 500] Past 100 steps: Average Loss 0.467 | Accuracy: 89%
# [Step 600] Past 100 steps: Average Loss 0.399 | Accuracy: 87%
# [Step 700] Past 100 steps: Average Loss 0.583 | Accuracy: 83%
# [Step 800] Past 100 steps: Average Loss 0.325 | Accuracy: 89%
# [Step 900] Past 100 steps: Average Loss 0.440 | Accuracy: 86%
# [Step 1000] Past 100 steps: Average Loss 0.434 | Accuracy: 85%
#
# --- Testing the CNN ---
# Test Loss: 0.5011615711838817
# Test Accuracy: 0.839
#
# Process finished with exit code 0
