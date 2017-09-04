#! /usr/bin/python3
# coding=utf-8
'''
  ffnetlib.py
'''


from flask import Flask

def wsgiLib():
  from wsgiref.simple_server import make_server
  
  def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

  httpd = make_server('', 12321, application)
  print('Serving HTTP on port 12321...')
  httpd.serve_forever()

def flaskLib():
  app = Flask(__name__)

  @app.route('/')
  def index():
    return('index')

  @app.route('/hello')
  def hello_world():
    return('Hello')
  
  app.run(host='0.0.0.0',debug=True)
  

def test():
  wsgiLib()

  
if(__name__ == '__main__'):
  test()

