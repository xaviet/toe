#! /usr/bin/python3
# coding=utf-8
'''
  mtpltlib.py
  ref : http://matplotlib.org/examples/index.html
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from mpl_toolkits.mplot3d import Axes3D
import time


def test1():
  fig = plt.figure()
  ax = Axes3D(fig)
  X = np.arange(-4, 4, 0.25)
  Y = np.arange(-4, 4, 0.25)
  X, Y = np.meshgrid(X, Y)
  R = np.sqrt(X**2 + Y**2)
  Z = np.sin(R)

  ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
  ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)
  ax.set_zlim(-2,2)

  #plt.savefig('../plot3d_ex.png',dpi=48)
  plt.show()
  time.sleep(1)
  plt.close('all')
  

def test():
  a = [i for i in range(256)]
  b = [(random.random(),random.random()) for i in a]
  fig1 = plt.figure(1)
  plt.plot(a,b)
  plt.show()
  

if (__name__ == '__main__'):
  test1()
