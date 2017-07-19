#! /usr/bin/python3
# coding=utf-8
'''
  mailclientlib.py
'''

import maillib
import os
import commonlib
import time

def test():
  maillib.mbC2SSend('ps aux|grep python3\ndate')
  time.sleep(1)
  t_rx = maillib.mbCRx()
  t_mbNumber = len(t_rx)
  commonlib.msg(str(t_mbNumber))
  for t_el0 in t_rx:
    for t_el1 in t_el0:
      print(t_el1)


if (__name__ == '__main__'):
  test()
