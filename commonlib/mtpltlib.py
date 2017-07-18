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


def test():
  a = [i for i in range(256)]
  b = [random.random() for i in a]
  fig1 = plt.figure(a, b)
  plt.show()


if (__name__ == '__main__'):
  test()
