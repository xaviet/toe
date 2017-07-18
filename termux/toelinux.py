#! /usr/bin/python3
# coding=utf-8
'''
  toelinux.py
'''

import doctest
import sys
import os
sys.path.append('..{0}commonlib'.format(os.sep))
import commonlib
sys.path.append('..{0}toelinux'.format(os.sep))
import liblinux


def test():
  print(commonlib.getSystem())
  print(liblinux.getCh())
  print(liblinux.callLibC().callC())


if (__name__ == '__main__'):
  test()
