#! /usr/bin/python3
# coding=utf-8
'''
  zipfilelib.py
'''

import zipfile
import os
import time


def zipfilelib(testFile):
  with zipfile.ZipFile('1.zip', 'w') as zf:
    zf.write(testFile)
    zf.write('ex.py')
  time.sleep(1)
  with zipfile.ZipFile('1.zip', 'r') as zf:
    print(zf.namelist())
    print(zf.infolist())
    print(zf.read(testFile).decode('utf-8'))


def makeFile(testFile):
  content = 'test zipfile\n\n1234567890\nabcdefghijklmnopqrstuvwxyz'
  f = open(testFile, 'w')
  f.write(content)
  f.close
  print(testFile in os.listdir())


def clean(testFile):
  os.remove(testFile)
  os.remove('1.zip')
  print(testFile in os.listdir())


def test():
  testFile = '1.txt'
  makeFile(testFile)
  zipfilelib(testFile)
  clean(testFile)


if (__name__ == '__main__'):
  test()
