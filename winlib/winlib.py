#!python
# coding=utf-8
'''
  libwin.py
'''

import doctest
import ctypes
import sys
import os
sys.path.append('..{0}commonlib'.format(os.sep))
import commonlib


def callLibC():
  '''
    Windows: '..{0}x64{0}Release{0}libwin.dll'.format(os.sep)
  '''
  dllPath = '..{0}x64{0}Release{0}libwin.dll'.format(os.sep)
  return (ctypes.CDLL(dllPath))


def getCh():
  '''
    Windows getCh()
  '''
  return (chr(callLibC().getCh()))


if (__name__ == '__main__'):
  pass
  doctest.testmod()
  lib = callLibC()
  print(lib.subtract(127, 255))
  print(getCh())
