from Read_MNIST import *

def makeTrainDataset(lenght) :
    data = []
    mnist = MNIST()
    test , label = mnist.load('train-images-idx3-ubyte','train-labels-idx1-ubyte')
    i = 0
    for record in test:
        record.append(label[i])
        i+=1
    i = 0
    while i < lenght:
        data.append(test[i])
        i += 1
    return data

def makeTestDataset(lenght):
    data = []
    targetAttr = []
    mnist = MNIST()
    test, label = mnist.load( 't10k-images-idx3-ubyte', 't10k-labels-idx1-ubyte' )
    i = 0
    while i < lenght:
        data.append( test[i] )
        targetAttr.append(label[i])
        i += 1
    return data , targetAttr

def makeValisdationSet(lenght):
    data = []
    validation = []
    mnist = MNIST()
    test, label = mnist.load( 'train-images-idx3-ubyte', 'train-labels-idx1-ubyte' )
    i = 0
    for record in test:
        record.append( label[i] )
        i += 1
    l = int((2*lenght)/3)
    valLenght = lenght - l
    i = 0
    for j in range(l):
        data.append(test[j])
        i += 1
    for j in range(valLenght):
        validation.append(test[i])
        i += 1
    return data,validation