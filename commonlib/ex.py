#! /usr/bin/python3
# coding=utf-8
'''
  ex.py
'''


from wsgiref.simple_server import make_server


def application(environ, start_response):
  start_response('200 OK', [('Content-Type', 'text/html')])
  return [b'<h1>Hello, web!</h1>']


httpd = make_server('', 12321, application)
print('Serving HTTP on port 12321...')
httpd.serve_forever()
