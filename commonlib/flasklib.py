#! /usr/bin/python3
# coding=utf-8
'''
  ffnetlib.py
'''


from flask import Flask

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
  flaskLib()

  
if(__name__ == '__main__'):
  test()

