#! /usr/bin/python3
# coding=utf-8
'''
  orangepiserver.py
'''

import maillib
import os
import commonlib
import time


def test():
  while (True):
    try:
      pass
      t_rx = []
      t_rx = maillib.mbSRx()
    except Exception as e:
      pass
      commonlib.msg(str(e))
      continue
    t_mbNumber = len(t_rx)
    commonlib.msg(str(t_mbNumber))
    for t_el0 in range(0, t_mbNumber):
      t_rt = ''
      for t_el1 in t_rx[t_el0]:
        t_cmd = os.popen(t_el1)
        t_rt = t_rt + '[# {0}]\n{1}\n'.format(t_el1, t_cmd.read())
      print(t_rt)
      maillib.mbS2CSend(t_rt)
    time.sleep(256)


if (__name__ == '__main__'):
  test()
