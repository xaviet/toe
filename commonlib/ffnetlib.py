#! /usr/bin/python3
# coding=utf-8
'''
  ffnetlib.py
'''


def test():
  from ffnet import mlgraph, ffnet
  import networkx as NX
  import pylab
  conec1 = mlgraph((2,2,2), biases=False)
  net1 = ffnet(conec1)
  conec2 = mlgraph((4,2,2,1), biases=True)
  net2 = ffnet(conec2)
  NX.draw_graphviz(net1.graph, prog='dot')
  pylab.show()


if (__name__ == '__main__'):
  test()
