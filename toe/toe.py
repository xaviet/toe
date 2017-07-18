#! /usr/bin/python3
# coding=utf-8
'''
  toe.py
'''

import doctest
import sys
import os
sys.path.append('..{0}commonlib'.format(os.sep))
sys.path.append('..{0}winlib'.format(os.sep))
import commonlib
import winlib
import matplotlib.pyplot as plt
import numpy as np
from prompt_toolkit import prompt


@commonlib.spentTime
def callLibC():
  print(libwin.callLibC().fibonacci(32))
  ann.test()


class cBoard():
  def __init__(self, **kwargs):
    self.view = [[1, 0, 0] for i in range(9)]

  def getView(self):
    return (self.view)

  def discriminator(self, side):
    '''
      return Ture:win False:other
    '''
    rt = False
    winBoard = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for el in winBoard:
      if (self.view[el[0]][side] == self.view[el[1]][side] ==
          self.view[el[2]][side] == 1):
        rt = True
        break
    return (rt)

  def steps(self):
    rt = 0
    for el in self.view:
      if (el[0] == 0):
        rt += 1
    return (rt)

  def play(self, pos):
    '''
      return 0:normal 1:break rule 2:win
    '''
    rt = 0
    if (8 < pos or pos < 0):
      rt = 1
    elif (self.view[pos][0] == 0):
      rt = 1
    else:
      side = self.steps() % 2 + 1
      self.view[pos][side] = 1
      self.view[pos][0] = 0
      if (self.discriminator(side)):
        rt = 2
    return (rt)


def sensor(view):
  rt = []
  for el0 in view:
    for el1 in el0:
      rt.append(el1)
  return (rt)


def exciter(resualt):
  rt = -1
  s = sum(resualt)
  if (s == 1):
    for i in range(len(resualt)):
      if (resualt[i] == 1):
        rt = i
  return (rt)


def poundGan():
  b = cBoard()
  print(sensor(b.getView()))
  print(exciter([0, 0, 0, 0, 0, 0, 1, 0, 0]))
  resault = 0
  while (True):
    pos = input('play:')
    print(pos)
    resault = b.play(int(pos))
    print(resault)
    if (resault != 0):
      break


def drawPicture():
  x = np.linspace(-10, 10, 1000)  #将-10到10等区间分成1000份
  print(type(x))
  y = 1 / (1 + np.exp(-x))
  plt.plot(x, y)
  plt.show()


def prmpt():
  while (True):
    cmd = prompt(' > ')
    print(cmd)
    if (cmd == 'exit'):
      break


def test():
  drawPicture()
  prmpt()


if (__name__ == '__main__'):
  test()
