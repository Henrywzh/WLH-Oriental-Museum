from tensorflow import keras
import numpy as np
import math
import matplotlib.pyplot as plt
import random

class Activation:
     def sigmoid(self, x):
          eqn = 1/(1+(math.e)**(-1*x))
          return eqn

     def relu(self, x):
          return np.maximum(0, x)

     def leakyRelu(self, x):
          if x <= 0:
               return 0.01 * x
          else:
               return x

     def tanh(self, x):
          eqn = 2*self.sigmoid(2*x) - 1
          return eqn

     def softmax(self, x):
          exp = np.exp(x - np.max(x))
          eqn = exp / exp.sum(axis=0)
          return eqn

     def dRelu(self, x):
          return x > 0

class Neuron:
     def parameters(self):
          w1 = np.random.randn(10, 784) * np.sqrt(2/784)
          b1 = np.zeros((10, 1))
          w2 = np.random.randn(10, 10) * np.sqrt(2/10)
          b2 = np.zeros((10, 1))
          return w1, b1, w2, b2

     def forward(self, x, w1, b1, w2, b2):
          act = Activation()
          z1 = w1.dot(x) + b1
          a1 = act.relu(z1)
          z2 = w2.dot(a1) + b2
          a2 = act.softmax(z2)
          return z1, a1, z2, a2

     def Y(self, y):
          actualY = np.zeros((y.max()+1, y.size))
          actualY[y, np.arange(y.size)] = 1
          return actualY

     def backward(self, x, y, a1, a2, w2, z1, m):
          act = Activation()
          actualY = self.Y(y)
          dz2 = a2 - actualY
          dw2 = dz2.dot(a1.T) / m
          db2 = np.sum(dz2, 1) / m
          dz1 = w2.T.dot(dz2) * act.dRelu(z1)
          dw1 = dz1.dot(x.T) / m
          db1 = np.sum(dz1, 1) / m
          return dw1, db1, dw2, db2

     def momentumDescent(self, x, y, learningRate, iterations, momentum):
          _, m = x.shape
          w1, b1, w2, b2 = self.parameters()
          vw1 = np.zeros((10, 784))
          vb1 = np.zeros((10, 1))
          vw2 = np.zeros((10, 10))
          vb2 = np.zeros((10, 1))

          for i in range(iterations + 1):
               z1, a1, z2, a2 = self.forward(x, w1, b1, w2, b2)
               dw1, db1, dw2, db2 = self.backward(x, y, a1, a2, w2, z1, m)

               vw1 = momentum * vw1 - learningRate * dw1
               vb1 = momentum * vb1 - learningRate * np.reshape(db1, (10,1))
               vw2 = momentum * vw2 - learningRate * dw2
               vb2 = momentum * vb2 - learningRate * np.reshape(db2, (10,1))

               w1 += vw1
               b1 += vb1
               w2 += vw2
               b2 += vb2

               if i % 100 == 0:
                    print(f'Iteration: {i} / {iterations}')
                    prediction = ai.predictions(a2)
                    print(f'{self.accuracy(prediction, trainY):.3%}')

          return w1, b1, w2, b2

     def adagrad(self,x, y, learningRate, iterations, eps=1e-8):
          size, m = x.shape
          w1, b1, w2, b2 = self.parameters()
          cdw1 = np.zeros((10, 784))
          cdb1 = np.zeros((10, 1))
          cdw2 = np.zeros((10, 10))
          cdb2 = np.zeros((10, 1))

          for i in range(iterations + 1):
               z1, a1, z2, a2 = self.forward(x, w1, b1, w2, b2)
               dw1, db1, dw2, db2 = self.backward(x, y, a1, a2, w2, z1, m)
               cdw1 += dw1**2
               w1 -= learningRate * dw1 / (np.sqrt(cdw1) + eps)
               cdb1 += np.reshape(db1, (10,1))**2
               b1 -= learningRate * np.reshape(db1, (10,1)) / (np.sqrt(cdb1) + eps)
               cdw2 += dw2**2
               w2 -= learningRate * dw2 / (np.sqrt(cdw2) + eps)
               cdb2 += np.reshape(db2, (10,1))**2
               b2 -= learningRate * np.reshape(db2, (10,1)) / (np.sqrt(cdb2) + eps)

               if i % 100 == 0:
                    print(f'Iteration: {i} / {iterations}')
                    prediction = ai.predictions(a2)
                    print(f'{self.accuracy(prediction, trainY):.3%}')

          return w1, b1, w2, b2

     def update(self, learningRate, w1, b1, w2, b2, dw1, db1, dw2, db2):
          w1 -= learningRate * dw1
          b1 -= learningRate * np.reshape(db1, (10,1))
          w2 -= learningRate * dw2
          b2 -= learningRate * np.reshape(db2, (10,1))
          return w1, b1, w2, b2

     def gradientDescent(self, x, y, learningRate, iterations):
          size, m = x.shape
          w1, b1, w2, b2 = self.parameters()

          for i in range(iterations + 1):
               z1, a1, z2, a2 = self.forward(x, w1, b1, w2, b2)
               dw1, db1, dw2, db2 = self.backward(x, y, a1, a2, w2, z1, m)
               w1, b1, w2, b2 = self.update(learningRate, w1, b1, w2, b2, dw1, db1, dw2, db2)
               if i % 100 == 0:
                    print(f'Iteration: {i} / {iterations}')
                    prediction = ai.predictions(a2)
                    print(f'{self.accuracy(prediction, trainY):.3%}')

          return w1, b1, w2, b2

     def predictions(self, a2):
          return np.argmax(a2, 0)

     def accuracy(self, predictions, y):
          return np.sum(predictions == y) / y.size

class Recognition:
     def guessing(self, x, w1 ,b1, w2, b2):
          ai = Neuron()
          _, _, _, A2 = ai.forward(x, w1, b1, w2, b2)
          predict = ai.predictions(A2)
          return predict

     def testing(self, x, w1, b1, w2, b2):
          fig, ax = plt.subplots(3,3)
          for i in range(3):
               for j in range(3):
                    index = random.randint(0, 10000)
                    image = x[:, index, None]
                    guess = self.guessing(image, w1, b1, w2, b2)

                    image = image.reshape((28, 28))
                    ax[i,j].set_ylabel(f'Predicts: {guess[0]}')
                    ax[i,j].imshow(image)
                    ax[i,j].grid(False)
          fig.colorbar(ax[0,0].imshow(image), ax=ax, orientation='horizontal')
          plt.show()

if __name__ == '__main__':
     data1 = keras.datasets.mnist
     data2 = keras.datasets.fashion_mnist
     (trainX, trainY), (testX, testY) = data1.load_data()

     columns = trainX.shape[1]
     rows = trainX.shape[2]
     trainX = trainX.reshape(trainX.shape[0], columns * rows).T / 255
     testX = testX.reshape(testX.shape[0], columns * rows).T  / 255

     ai = Neuron()
     learningRate = 0.05
     iterations = 500
     momentum = 0.9

     # w1, b1, w2, b2 = ai.gradientDescent(trainX, trainY, learningRate, iterations)
     w1, b1, w2, b2 = ai.momentumDescent(trainX, trainY, learningRate, iterations, momentum)
     # w1, b1, w2, b2 = ai.adagrad(trainX, trainY, learningRate, iterations)

     _, _, _, a2 = ai.forward(testX, w1, b1, w2, b2)
     prediction = ai.predictions(a2)
     print(f'Accuracy: {ai.accuracy(prediction, testY):.3%}')

     OCR = Recognition()
     OCR.testing(testX, w1, b1, w2, b2)
