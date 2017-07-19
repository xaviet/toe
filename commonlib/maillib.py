#! /usr/bin/python3
# coding=utf-8
'''
  mail.py
'''

import logging
logging.basicConfig(level=logging.DEBUG)
import poplib
import smtplib
import email.mime.multipart
import email.mime.text
import commonlib
from commonlib import crypto, detectCharSet
import time


def getMbFormat():
  '''
    get mb format
    return format
  '''
  return ('{0}{3}{2}{1}{4}')


def getMbInner():
  '''
    get mb inner
    return mb
  '''
  return (getMbFormat().format('toe_inn', '6.c', '2', 'er@1', 'om'))


def getMbOuter():
  '''
    get mb outer
    return mb
  '''
  return (getMbFormat().format('toe_out', '6.c', '2', 'er@1', 'om'))


def getRxUrl():
  '''
    get receive url
    return url
  '''
  return (getMbFormat().format('po', '6.c', '2', 'p3.1', 'om'))


def getTxUrl():
  '''
    get transport url
    return url
  '''
  return (getMbFormat().format('sm', '6.c', '2', 'tp.1', 'om'))


def getPp():
  '''
    get pp
    return pp
  '''
  return (getMbFormat().format('76', 'to', '29', '08', 'e'))


def mbTx(v_mbFrom, v_mbTo, v_subject, v_content, v_pp):
  '''
    mb tx

  '''
  t_mb = email.mime.multipart.MIMEMultipart()
  t_mb['from'] = v_mbFrom
  t_mb['to'] = v_mbTo
  t_mb['subject'] = v_subject
  t_mb.attach(email.mime.text.MIMEText(crypto(v_content)))
  t_smtp = smtplib.SMTP_SSL(getTxUrl())
  #t_smtp=smtplib.SMTP()
  #t_smtp.connect(getTxUrl())
  t_smtp.login(v_mbFrom, v_pp)
  t_smtp.sendmail(v_mbFrom, v_mbTo, str(t_mb))
  t_smtp.quit()


def mbRx(v_mb, v_pp, v_keyString):
  '''
    mb rx

  '''
  t_mb = poplib.POP3_SSL(getRxUrl())
  #t_mb=poplib.POP3(getRxUrl())
  t_mb.user(v_mb)
  t_mb.pass_(v_pp)
  t_mNumber = t_mb.stat()
  t_rt = []
  t_contentFlag = False
  for i in range(1, t_mNumber[0] + 1):
    #t_mlist=t_mb.top(i,1)
    t_mContent = []
    for t_l in t_mb.retr(i)[1]:
      t_line = crypto(t_l.decode(detectCharSet(t_l)))
      if (t_contentFlag):
        t_mContent.append(t_line)
      if (t_line == 'c/s %s 0' % (v_keyString, )):
        t_contentFlag = True
      if ((t_mContent != [])
          and (t_line == 'c/s %s 1' % (v_keyString, ))):
        t_rt.append(t_mContent[:-1])
        t_contentFlag = False
    t_mb.dele(i)
  t_mb.quit()
  return (t_rt)


def mbC2SSend(v_content):
  '''
    send mail from client to server

  '''
  mbTx(getMbOuter(),
       getMbInner(), 'pioevh\'s operation',
       '\nc/s client 0\n%s\nc/s client 1\n' % (v_content, ), getPp())


def mbS2CSend(v_content):
  '''
    send mail from server to client

  '''
  mbTx(getMbInner(),
       getMbOuter(), 'pioevh\'s operation',
       '\nc/s server 0\n%s\nc/s server 1\n' % (v_content, ), getPp())


def mbCRx():
  '''
    receive mail from client

  '''
  return (mbRx(getMbOuter(), getPp(), 'server'))


def mbSRx():
  '''
    receive mail from server

  '''
  return (mbRx(getMbInner(), getPp(), 'client'))


def test():
  mbC2SSend('dir\ndate')
  time.sleep(1)
  t_rx = mbCRx()
  t_mbNumber = len(t_rx)
  commonlib.msg(str(t_mbNumber))
  for t_el0 in t_rx:
    for t_el1 in t_el0:
      print(t_el1)


if (__name__ == '__main__'):
  test()
