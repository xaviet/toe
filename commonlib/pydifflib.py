#!python
# coding=utf-8
'''
  pydifflib.py
'''


import os


def pydiff():
  whla=[]
  for el0 in os.listdir('D:\\temp\\python3.6'):
    whla.append((el0.split('-'))[0].replace('_','-'))
  enva=[]
  envf=open('requirements.txt','r')
  for el0 in envf:
    enva.append((el0.split('='))[0])
  print(sorted(set(enva).difference(set(whla))))
  print(sorted(set(whla).difference(set(enva))))

if(__name__=='__main__'):
  pydiff()  