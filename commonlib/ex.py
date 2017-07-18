from ffnet import imlgraph, ffnet
import networkx as NX
import pylab

conec = imlgraph((3, [(3, ), (6, 3), (3, )], 3), biases=False)
net = ffnet(conec)
NX.draw_networkx(net.graph, prog='dot')
pylab.show()
