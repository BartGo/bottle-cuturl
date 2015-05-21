# -*- coding: utf-8 -*-
from bottle import Bottle, view, static_file


home_app = Bottle()


@home_app.route('/')
@view('index.html')
def index():
  return {'get_url': home_app.get_url}
  