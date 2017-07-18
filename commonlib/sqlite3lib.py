#! /usr/bin/python3
# coding=utf-8
'''
  sqlt3lib.py
'''

import sqlite3


def sqliteOpt(v_db, v_opt):
  '''
    sqlite3 single operate
    return result
  '''
  t_rtArray = []
  t_dbCon = sqlite3.connect(v_db)
  t_dbCur = t_dbCon.cursor()
  t_dbCur.execute(v_opt)
  t_rtArray = t_dbCur.fetchall()
  t_dbCon.commit()
  t_dbCur.close()
  t_dbCon.close()
  return (t_rtArray)


def sqliteOptBatch(v_db, v_opt):
  '''
    sqlite3 batch operate
  '''
  t_dbCon = sqlite3.connect(v_db)
  t_dbCur = t_dbCon.cursor()
  for t_el in v_opt:
    t_dbCur.execute(t_el)
  t_dbCon.commit()
  t_dbCur.close()
  t_dbCon.close()
  return (0)


class sqliteMemory():
  def __init__(self):
    self.dbCon = sqlite3.connect(':memory:')

  def opt(self, opt):
    cur = self.dbCon.cursor()
    cur.execute(opt)
    rt = cur.fetchall()
    self.dbCon.commit()
    cur.close()
    return (rt)

  def batch(self, optList):
    cur = self.dbCon.cursor()
    for el in optList:
      cur.execute(el)
    self.dbCon.commit()
    cur.close()
    return (0)

  def closeDb(self):
    self.dbCon.close()


def test():
  md = sqliteMemory()
  md.opt('create table t(id int)')
  md.opt('insert into t(id) values(11)')
  print(md.opt('select * from t')[0])
  md.batch(('insert into t(id) values(211)',
            'insert into t(id) values(1211)',
            'insert into t(id) values(11211)'))
  print(md.opt('select * from t'))
  md.closeDb()


if (__name__ == '__main__'):
  test()
