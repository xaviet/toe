#!python
# coding=utf-8
'''
  mtpltlib.py
  ref : http://matplotlib.org/examples/index.html
'''


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


def main():
  a=[i for i in range(256)]
  b=[random.random() for i in a ]
  plt.plot(a,b)
  plt.show()

if(__name__=='__main__'):
  main()