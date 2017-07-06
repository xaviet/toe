#!python
# coding=utf-8
'''
  mtpltlib.py
  ref : http://matplotlib.org/examples/index.html
'''


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def main():
  a=[i for i in range(16)]
  b=[i * i - i ** 1.5 for i in a ]
  plt.plot(a,b)
  plt.show()

if(__name__=='__main__'):
  main()