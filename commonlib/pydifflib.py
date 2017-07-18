#! /usr/bin/python3
# coding=utf-8
'''
  pydifflib.py
'''

import os


def test():
  pylibPath = 'D:{0}temp{0}python3.6'.format(os.sep)
  pylibPath = pylibPath if (os.path.exists(pylibPath)
                            ) else 'D:{0}media{0}pypi'.format(os.sep)
  whla = []
  for el0 in os.listdir(pylibPath):
    whla.append((el0.split('-'))[0].replace('_', '-'))
  enva = []
  envf = open('requirements.txt', 'r')
  for el0 in envf:
    enva.append((el0.split('='))[0])
  print(sorted(set(enva).difference(set(whla))))
  print(sorted(set(whla).difference(set(enva))))


if (__name__ == '__main__'):
  test()
