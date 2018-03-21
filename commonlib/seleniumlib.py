#! /usr/bin/python3
# coding=utf-8
'''
  seleniumlib.py
'''

import commonlib


def test():
  import time
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
  #driver.maximize_window()
  driver.get('http://172.28.73.8/c6/Jhsoft.Web.login/PassWordNew.aspx')
  #driver.get('http://172.28.72.18:8080/qcbin')
  driver.find_element_by_name('UserName').send_keys("xujin")
  driver.find_element_by_name('Password2').send_keys("13971146175")
  driver.find_element_by_id('btnLogin').click()
  time.sleep(8)
  windows = driver.window_handles
  driver.close()
  driver.switch_to.window(windows[-1])
  
  #driver.find_element_by_id('toolbarmenu').click()
  #time.sleep(8)
  driver.execute_script('menuclick(\'01\',\'上班签到\',\'../JHSoft.web.HRMAttendance/attendance_on.aspx\',\'003000800010\');win_PopMenu.SetVisted(\'01\',\'上班签到\',\'../JHSoft.web.HRMAttendance/attendance_on.aspx\',\'003000800010\');')
  time.sleep(8)
  driver.switch_to_frame('imain_2')
  print(driver.find_element_by_id('LCurTime').text)
  driver.find_element_by_id('btn_ok').click()
  time.sleep(8)
  input()
  driver.close()


if (__name__ == '__main__'):
  test()
