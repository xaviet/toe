#! /usr/bin/python3
# coding=utf-8
'''
  prompt_toolkitlib.py
'''


from prompt_toolkit import prompt


def test():
  while (True):
    cmd = prompt(' > ')
    print(cmd)
    if (cmd == 'exit'):
      break
      

if (__name__ == '__main__'):
  test()
