#! /usr/bin/python3
# coding=utf-8
'''
  routelib.py
'''

import commonlib
import copy


pathFlag = False

def getZero(pa):
  c = 0
  for el0 in pa:
    for el1 in el0:
      if(el1 == 0):
        c += 1
  return(c)


def pathClean(ta, x, y, steps, route, i, j):
  if(ta[x + i][y + j] == 0):
    ta[x + i][y + j] = 2;
    steps -= 1
    #print([x + i, y + j], steps)
    route.append([x + i, y + j])
    pathClean(ta, x + i, y + j, steps, route, i, j)
  else:
    startClean(ta, x, y, steps, route)


def startClean(pa, x, y, steps, route):
  global pathFlag
  ta = copy.deepcopy(pa)
  ta[x][y] = 8
  #print(ta[x][y])
  #print('start...', [x, y], steps)
  #commonlib.arrayPrintFormat(ta)
  if(steps == 0):
    #print(route)
    c = 2
    for el0 in route:
      ta[el0[0]][el0[1]] = c
      c += 1
      if(c > 9):
        c = 3
    commonlib.arrayPrintFormat(ta)
    #print('startClean return True')
    pathFlag = True
  else:
    if(ta[x - 1][y] == 0 and pathFlag == False):
      pathA = copy.deepcopy(ta)
      pathRoute = copy.deepcopy(route)
      #, print('up')
      pathClean(pathA, x, y, steps, pathRoute, -1, 0)
    if(ta[x + 1][y] == 0 and pathFlag == False):
      pathA = copy.deepcopy(ta)
      pathRoute = copy.deepcopy(route)
      #, print('down')
      pathClean(pathA, x, y, steps, pathRoute, 1, 0)
    if(ta[x][y - 1] == 0 and pathFlag == False):
      pathA = copy.deepcopy(ta)
      pathRoute = copy.deepcopy(route)
      #, print('left')
      pathClean(pathA, x, y, steps, pathRoute, 0, -1)
    if(ta[x][y + 1] == 0 and pathFlag == False):
      pathA = copy.deepcopy(ta)
      pathRoute = copy.deepcopy(route)
      #, print('right')
      pathClean(pathA, x, y, steps, pathRoute, 0, 1)


def cleanRoom():
  global pathFlag
  pa = \
  [\
    [1, 1, 1, 1, 1, 1, 1], \
    [1, 0, 0, 1, 1, 1, 1], \
    [1, 0, 1, 0, 0, 0, 1], \
    [1, 0, 0, 0, 0, 0, 1], \
    [1, 1, 0, 0, 0, 0, 1], \
    [1, 1, 0, 0, 0, 0, 1], \
    [1, 1, 1, 1, 1, 1, 1], \
   ]
  #commonlib.arrayPrintFormat(pa)
  #print(getZero(pa))
  for el0 in range(1, 6):
    for el1 in range(1, 6):
      if(pa[el0][el1] == 0):
        route=[]
        steps = getZero(pa) - 1
        route.append([el0, el1])
        #print('begin...', [el0, el1])
        #commonlib.arrayPrintFormat(pa)
        startClean(pa, el0, el1, steps, route)
        if(pathFlag == True):
          print('end...')
          return(0)
        else:
          continue
  print('No route')
  return(1)


if (__name__ == '__main__'):
 cleanRoom()
