#!python
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


def pyFormat(path):
  '''
    yapf -r -i -p d:\code\toe --style="{based_on_style:pep8, column_limit:96, indent_width:2}"
  '''
  pass


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
  t_types = ['utf-8', 'unicode', 'gb2312', 'gbk', 'gb18030', 'big5', 'us-ascii', 'unknow']
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
  #return(v_str)


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


def main():
  pass

  def ex(n):
    a = list(range(0, n))
    while (len(a) > 1):
      b = a[1::2]
      a = b
    return (a[0])

  def ex1(n):
    m = 1
    while ((2 * m) <= n):
      m *= 2
    return (m - 1)

  for i in range(1, 15):
    print(i, ex(i), ex1(i))


if (__name__ == '__main__'):
  pass
  main()