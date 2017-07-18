#! /usr/bin/python3
# coding=utf-8
'''
  ffnetlib.py
'''

from ffnet import ffnet, mlgraph, savenet, loadnet, exportnet
import networkx as NX
import pylab


def test():
  conec = mlgraph((2, 2, 1))
  net = ffnet(conec)
  input = [[0., 0.], [0., 1.], [1., 0.], [1., 1.]]
  target = [[1.], [0.], [0.], [1.]]
  net.train_tnc(input, target, maxfun=1000)
  net.test(input, target, iprint=2)
  #savenet(net, "xor.net")
  #exportnet(net, "xor.f")
  #net = loadnet("xor.net")
  answer = net([0., 0.])
  partial_derivatives = net.derivative([0., 0.])

  NX.draw_networkx(net.graph, prog='dot')
  pylab.show()


if (__name__ == '__main__'):
  test()