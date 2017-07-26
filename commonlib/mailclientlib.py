#! /usr/bin/python3
# coding=utf-8
'''
  mailclientlib.py
'''

import maillib
import os
import commonlib
import time
from prompt_toolkit import prompt


def mailClient():
  while (True):
    cmd = prompt('> ')
    #print(cmd)
    if (cmd == 'exit'):
      break
    try:
      maillib.mbC2SSend(cmd)
      time.sleep(maillib.mbAccessInterval())
      t_rx = maillib.mbCRx()
      t_mbNumber = len(t_rx)
      commonlib.msg(str(t_mbNumber))
      for t_el0 in t_rx:
        for t_el1 in t_el0:
          print(t_el1)
    except:
      print('mb fault!\n')


def test():
  mailClient()


if (__name__ == '__main__'):
  test()
