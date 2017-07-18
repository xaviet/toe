#! /usr/bin/python3
# coding=utf-8
'''
  seleniumlib.py
'''

import commonlib


def test():
  import os
  import sys
  from selenium import webdriver
  from selenium.webdriver.common.keys import Keys
  if (commonlib.getSystem() == 87):
    ffPath = 'D:{0}app{0}firefox{0}App{0}Firefox64{0}'.format(os.sep)
    ffPath = ffPath if (os.path.exists(ffPath)) else 'C' + ffPath[1:]
    os.environ['Path'] = os.environ['Path'] + ';' + ffPath
    sys.path.append('{0}geckodriver.exe'.format(ffPath))
    sys.path.append('{0}firefox.exe'.format(ffPath))
  driver = webdriver.Firefox()
  driver.maximize_window()
  driver.get('http://www.lfd.uci.edu/~gohlke/pythonlibs/')
  elem = driver.find_element_by_tag_name('p')
  print(elem)
  elem.clear()
  driver.close()


if (__name__ == '__main__'):
  test()
