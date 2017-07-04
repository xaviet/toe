#!python
# coding=utf-8
'''
  liblinux.py
'''

import doctest
import ctypes
import sys
import os
sys.path.append('..{0}commonlib'.format(os.sep))
import commonlib


def callLibC():
  '''
    Linux: '..{0}termux{0}output{0}liblinux.so'.format(os.sep)
  '''
  dllPath = '..{0}termux{0}output{0}liblinux.so'.format(os.sep)
  return (ctypes.CDLL(dllPath))


def getCh():
  '''
    Linux getCh()
  '''
  ch = ''
  try:
    import sys, tty, termios
    pass
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno(), termios.TCSANOW)
    ch = sys.stdin.read(1)
    #sys.stdout.write(ch) #echo
  except:
    logging.debug('sys,tty,termios error!')
  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
  return (ch)


if (__name__ == '__main__'):
  print(getCh())
