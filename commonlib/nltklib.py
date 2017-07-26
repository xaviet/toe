#! /usr/bin/python3
# coding=utf-8
'''
  nltklib.py
  ref: http://www.burnelltek.com/blog/8658d836c36111e6841d00163e0c0e36
'''

import nltk
# data ready by nltk.download()
# keep default dictionary
from nltk.book import *


def test():
  #texts()
  text1.concordance('monstrous')
  text1.collocations()
  #text4.dispersion_plot(['freedom', 'America'])


if (__name__ == '__main__'):
  test()
