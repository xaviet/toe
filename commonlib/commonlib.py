#! /usr/bin/python3
# coding=utf-8
'''
  commonlib.py
'''

import doctest
import time
import logging
logging.basicConfig(level=logging.DEBUG)
import platform
import sys
import os
import ctypes
import multiprocessing
import base64

def pyFormat(path):
  '''
    yapf -r -i -p /home/pv/Documents/toe --style="{based_on_style:pep8, column_limit:72, indent_width:2}"
  '''
  pass


def getCpus():
  return (multiprocessing.cpu_count())


def getSystem():
  '''
    get system type
    return 87(Windows) or 76(Linux)
  '''
  return (ord(platform.system()[0]))


def spentTime(function):
  '''
    decorator spentTime
  '''

  def decoratorFun(*para):
    starttime = time.time()
    rt = function(*para)
    logging.debug('%s spentTime: ' % (function.__name__, ) + '%5.6f' %
                  ((time.time() - starttime), ) + ' s.')
    return (rt)

  return (decoratorFun)


def subtract(a, b):
  '''
    >>> subtract(127,255)
    -128
    >>> subtract(255,127)
    128
  '''
  return (a - b)


def floydAlgorithm(nm, pm, nodeNum):
  '''
    floyd  nm:pathCast  pm:nextHop nodeNum:nodeNumber
  '''
  for k in range(nodeNum):
    for i in range(nodeNum):
      for j in range(nodeNum):
        if ((nm[i][k] != -1) and (nm[k][j] != -1)
            and ((nm[i][k] + nm[k][j] < nm[i][j]) or (nm[i][j] == -1))):
          nm[i][j] = nm[i][k] + nm[k][j]
          pm[i][j] = pm[i][k]
  return (nm, pm)


@spentTime
def fibonacci(a):
  '''
    fibonacci
  '''
  fibonacciDict = {0: 0, 1: 1}

  def f(n):
    nonlocal fibonacciDict
    if (n in fibonacciDict):
      return (fibonacciDict[n])
    else:
      rt = f(n - 2) + f(n - 1)
      fibonacciDict[n] = rt
      return (rt)

  return (f(a))


def detectCharSet(v_data):
  '''
    detect character set
    return member in ['utf-8','unicode','gb2312','gbk','gb18030','big5','us-ascii','unknow']
  '''
  t_types = [
      'utf-8', 'unicode', 'gb2312', 'gbk', 'gb18030', 'big5',
      'us-ascii', 'unknow'
  ]
  for t_codetype in t_types:
    try:
      v_data.decode(t_codetype)
      return (t_codetype)
    except:
      continue
  else:
    return ('unknow')


def crypto(v_str):
  '''
    String encryption or decryption with symmetric algorithm
  '''
  t_d = {}
  for t_c in (65, 97):
    for t_i in range(26):
      t_d[chr(t_i + t_c)] = chr((t_i + 13) % 26 + t_c)
  return ((''.join([t_d.get(t_c, t_c) for t_c in v_str])))


def base64Encode(vString):
  return(base64.b64encode(vString.encode('utf-8')).decode('utf-8'))


def base64Decode(vString):
  return(base64.b64decode(vString.encode('utf-8')).decode('utf-8'))
  
  
def msg(v_msg, v_rollmode=True, v_newlinemode=True):
  '''
    print msg with roll and newline
  '''
  t_ctime = time.strftime('[%Y-%m-%d_%H:%M:%S] ', time.localtime())
  t_msg = ('\n' if (v_newlinemode) else '') + t_ctime + v_msg
  if (v_rollmode == False):
    sys.stdout.write('\r' + (' ' * 80) + '\r' + t_msg)
  else:
    print(t_msg)
  sys.stdout.flush()


def existMan(num, start, interval):
  def ex(num, start, interval):
    a = list(range(0, num))
    while (len(a) > (interval - 1)):
      b = a[start::interval]
      a = b
    return (a)

  def ex1(num):
    m = 1
    while ((2 * m) <= num):
      m *= 2
    return (m - 1)

  print(ex(num, start, interval))

def dispDataList(vList, maxValue=64):
  refData=max(vList)
  n=0
  for el0 in vList:
    n+=1
    print('%-4d'%(n,),'*'*int(maxValue*el0/refData))


def test():
  pass
  existMan(500, 1, 2)
  a = [[0, 10, 30, 50], [10, 0, 60, 20], [30, 60, 0, 40],
       [50, 20, 40, 0]]
  p = [[0, 1, 2, 3], [1, 0, 2, 3], [1, 2, 0, 3], [1, 2, 3, 0]]
  n = 4
  a, p = floydAlgorithm(a, p, n)
  print(a, p)

def arrayPrintFormat(array):
  if(type(array) == list and type(array[0]) == list):
    for el0 in array:
        arrayPrintFormat(el0)
  else:
    print(array)


if (__name__ == '__main__'):
  dispDataList([1,3,4,2,45,5,12,1,2,44,33,22,0,99])
  arrayPrintFormat([[[1,5],[2,6]],[[[3,7],[4,8]]]])