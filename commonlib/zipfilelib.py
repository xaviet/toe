#!python
# coding=utf-8
'''
  zipfilelib.py
'''


import zipfile
import os
import time


def zipfilelib(testFile): 
  content='test zipfile\n\n1234567890\nabcdefghijklmnopqrstuvwxyz'
  f=open(testFile,'w')
  f.write(content)
  f.close
  print(os.listdir())
  time.sleep(1)
   

def clean(testFile):
  os.remove(testFile)
  print(os.listdir())

if(__name__=='__main__'):
  testFile='test.txt'
  zipfilelib(testFile)
  clean(testFile)