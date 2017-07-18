#! /usr/bin/python3
# coding=utf-8
'''
  annlib.py
'''

import sys
import random
import multiprocessing
import time

import commonlib
import sqlt3


class unitCell():
  def __init__(self, **kwargs):
    pass


class neuron(unitCell):
  def __init__(self, **kwargs):
    dendriteNumber = kwargs.get('dendriteNumber', None)
    assert (dendriteNumber != None)
    self.dendrite = []
    self.dendriteWeight = []
    self.threshold = random.uniform(0, 1)
    return (super().__init__(**kwargs))

  def setDendrite(lastLayerNeuron):
    self.dendrite.append(lastLayerNeuron)
    self.dendriteWeight.append(random.uniform(-1, 1))

  def createSynapse(self, nextLayerNeuron):
    nextLayerNeuron.setDendrite(self)

  def activation(self):
    return (sum(
        list(
            map(lambda x, y: x.axon * y, self.dendrite,
                self.dendriteWeight))))

  @property
  def axon(self):
    return (1 if (self.activation() > self.threshold) else 0)


class neuronalNetwork():
  def __init__(self):
    pass


def fTimer(interval, sharedValue):
  while (sharedValue['running']):
    time.sleep(interval)
    sharedValue['timer'] += 1


@commonlib.spentTime
def test():
  pass
  dendriteNumber = 256
  neuronsPerHideLayer = 4 * dendriteNumber
  hideLayersNumber = 8
  neuronNumber = 0
  cells = []
  sharedValue = multiprocessing.Manager().dict()
  sharedValue['running'] = True
  sharedValue['timer'] = 0
  timer = multiprocessing.Process(target=fTimer, args=(1, sharedValue))
  timer.daemon = True
  timer.start()
  while (sharedValue['timer'] < 32):
    cells.append(neuron(dendriteNumber=dendriteNumber))
    neuronNumber += 1
  neuronsHideLayer = neuronsPerHideLayer * hideLayersNumber
  neuronsInputLayer = int((neuronNumber - neuronsHideLayer) / 2) + int(
      (neuronNumber - neuronsHideLayer) % 2)
  hideLayer = []
  for i in range(hideLayersNumber):
    hideLayer.append(
        cells[i * neuronsPerHideLayer:(i + 1) * neuronsPerHideLayer])
  InputLayer = cells[neuronsHideLayer:
                     neuronsHideLayer + neuronsInputLayer]
  OutputLayer = cells[neuronsHideLayer + neuronsInputLayer:]
  print(neuronNumber,
        len(InputLayer), len(OutputLayer), dendriteNumber * 4 * 8)
  sharedValue['running'] = False
  return (cells)


import numpy as np
if (__name__ == '__main__'):
  #test()
  X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
  y = np.array([[0, 1, 1, 0]]).T
  syn0 = 2 * np.random.random((3, 4)) - 1
  syn1 = 2 * np.random.random((4, 1)) - 1
  for j in range(60):
    l1 = 1 / (1 + np.exp(-(np.dot(X, syn0))))
    l2 = 1 / (1 + np.exp(-(np.dot(l1, syn1))))
    l2_delta = (y - l2) * (l2 * (1 - l2))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1 - l1))
    syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)
  c = 0
  nc = 0
  j = 1
  while (True):
    a = random.randint(1, 3)
    s = random.randint(1, 3)
    if (a == s):
      nc += 1
    else:
      c += 1
    print(j, c / j, nc / j)
    j += 1
'''
import math  
import random  
import string  
import pylab
import numpy
import time

#random.seed(0)  
random.seed(time.time())
#print(time.time())

# calculate a random number where:  a <= rand < b  
def rand(a,b):  
  return((b-a)*random.random()+a)
  
# Make a matrix (we could use NumPy to speed this up)  
def makeMatrix(I,J,fill=0.0):  
  m=[]  
  for i in range(I):  
    m.append([fill]*J)  
  return(m)  
  
# our sigmoid function, tanh is a little nicer than the standard 1/(1+e^-x)  
#使用双正切函数代替logistic函数  
def sigmoid(x):  
  return(math.tanh(x))
  
# derivative of our sigmoid function, in terms of the output (i.e. y)  
# 双正切函数的导数，在求取输出层和隐藏侧的误差项的时候会用到  
def dsigmoid(y):  
  return(1.0-y**2) 

class NN:  
  def __init__(self,ni,nh,no):  
    #print('__init__')
    # number of input, hidden, and output nodes  
    # 输入层，隐藏层，输出层的数量，三层网络  
    self.ni=ni + 1 # +1 for bias node  
    self.nh=nh  
    self.no=no  
  
    # activations for nodes  
    self.ai=[1.0]*self.ni  
    self.ah=[1.0]*self.nh  
    self.ao=[1.0]*self.no  
    #print(self.ai)  
    # create weights  
    #生成权重矩阵，每一个输入层节点和隐藏层节点都连接  
    #每一个隐藏层节点和输出层节点链接  
    #大小：self.ni*self.nh  
    self.wi=makeMatrix(self.ni,self.nh)  
    #大小：self.ni*self.nh  
    self.wo=makeMatrix(self.nh,self.no)  
    # set them to random vaules  
    #生成权重，在-0.2-0.2之间  
    for i in range(self.ni):  
      for j in range(self.nh):  
        self.wi[i][j]=rand(-0.1,0.1)  
    for j in range(self.nh):  
      for k in range(self.no):  
        self.wo[j][k]=rand(-0.1,0.1)  
#   print(self.wi)
#   print(self.wo)
    # last change in weights for momentum   
    #?  
    self.ci=makeMatrix(self.ni,self.nh)  
    self.co=makeMatrix(self.nh,self.no)  
  
  def update(self,inputs):  
    #print('update')
    if(len(inputs)!=self.ni-1):  
      raise ValueError('wrong number of inputs')  
  
    # input activations  
    # 输入的激活函数，就是y=x;  
    for i in range(self.ni-1):  
      #self.ai[i]=sigmoid(inputs[i])  
      self.ai[i]=inputs[i]  
    #print(self.ai)
    # hidden activations  
    #隐藏层的激活函数,求和然后使用压缩函数  
    for j in range(self.nh):  
      sum=0.0  
      for i in range(self.ni):  
        #sum就是《ml》书中的net  
        sum=sum+self.ai[i]*self.wi[i][j]  
      #print(sum)
      self.ah[j]=sigmoid(sum)  
      #print(self.ah[j])
    # output activations  
    #输出的激活函数  
    for k in range(self.no):  
      sum=0.0  
      for j in range(self.nh):  
        sum=sum + self.ah[j]*self.wo[j][k]  
      self.ao[k]=sigmoid(sum) 
    #print(sum)
    #print(self.ao)
    return(self.ao[:])
  
  #反向传播算法 targets是样本的正确的输出  
  def backPropagate(self,targets,N,M):  
    #print('backPropagate')
    if(len(targets)!=self.no):  
      raise ValueError('wrong number of target values')  
  
    # calculate error terms for output  
    #计算输出层的误差项   
    output_deltas=[0.0]*self.no  
    for k in range(self.no):  
      #计算k-o  
      error=targets[k]-self.ao[k]  
      #计算书中公式4.14  
      output_deltas[k]=dsigmoid(self.ao[k])*error 
    #print(targets) 
    #print(output_deltas)
    # calculate error terms for hidden  
    #计算隐藏层的误差项，使用《ml》书中的公式4.15  
    hidden_deltas=[0.0]*self.nh  
    for j in range(self.nh):  
      error=0.0  
      for k in range(self.no):  
        error=error+output_deltas[k]*self.wo[j][k]  
      hidden_deltas[j]=dsigmoid(self.ah[j])*error  
    #print(hidden_deltas)
    # update output weights  
    # 更新输出层的权重参数  
    # 这里可以看出，本例使用的是带有“增加冲量项”的BPANN  
    # 其中，N为学习速率 M为充量项的参数 self.co为冲量项  
    # N: learning rate  
    # M: momentum factor  
    for j in range(self.nh):  
      for k in range(self.no):  
        change=output_deltas[k]*self.ah[j]  
        self.wo[j][k]=self.wo[j][k]+N*change+M*self.co[j][k]  
        self.co[j][k]=change  
        #print N*change, M*self.co[j][k]  
    #print(self.wo)   
    # update input weights  
    #更新输入项的权重参数  
    for i in range(self.ni):  
      for j in range(self.nh):  
        change=hidden_deltas[j]*self.ai[i]  
        self.wi[i][j]=self.wi[i][j]+N*change+M*self.ci[i][j]  
        self.ci[i][j]=change  
    #print(self.wi)
    # calculate error  
    #计算E(w)  
    error=0.0  
    for k in range(len(targets)):  
      error=error+0.5*(targets[k]-self.ao[k])**2  
    #print(error)
    return(error)
    
  #测试函数，用于测试训练效果  
  def test(self,patterns):  
    for p in patterns:  
      print(p[0], '->', self.update(p[0]))  
  
  def weights(self):  
    print('Input weights:')  
    for i in range(self.ni):  
      print(self.wi[i])  
    print()  
    print('Output weights:')  
    for j in range(self.nh):  
      print(self.wo[j])  
  
  def train(self,patterns,iterations=1024,N=0.25,M=0.25):  
    # N: learning rate  
    # M: momentum factor  
    for i in range(iterations):  
      error=0.0  
      for p in patterns:  
        inputs=p[0]  
        targets=p[1]  
        self.update(inputs)  
        error=error+self.backPropagate(targets,N,M)  
        #input()
#       print(self.wi)
#       print(self.wo)
      if(i%100==0):  
        print('error %-.5f' % error) 

if(__name__ == '__main__'):
  pass
'''
