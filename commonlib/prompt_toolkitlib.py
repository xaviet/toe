#! /usr/bin/python3
# coding=utf-8
'''
  prompt_toolkitlib.py
  ref: https://github.com/jonathanslenders/python-prompt-toolkit/
'''


from prompt_toolkit import prompt


def test():
  print('This is multiline input. press [Meta+Enter] or [Esc] followed by [Enter] to accept input.')
  print('You can click with the mouse in order to select text.')
  answer = prompt('Multiline input: ', multiline=True, mouse_support=True)
  print('You said: %s' % answer)
  while (True):
    cmd = prompt('> ')
    print(cmd)
    if (cmd == 'exit'):
      break
      

if (__name__ == '__main__'):
  test()
