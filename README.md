# progressed-py

[![License](https://img.shields.io/github/license/RDCH106/progressed-py.svg)](https://github.com/RDCH106/progressed-py/blob/master/LICENSE)
[![Pypy](https://img.shields.io/badge/PyPy-3.5-ff69b4.svg)](https://pypy.org/)
[![Build Status](https://travis-ci.org/RDCH106/progressed-py.svg?branch=master)](https://travis-ci.org/RDCH106/progressed-py)

Progressbar microservice written in 🐍 Python

This is a Python 2.x & Python 3.x WSGI version of https://github.com/fehmicansaglam/progressed.io, so all credit
for the idea and original implementation is due to Fehmi Can Sağlam.

Aarni Koskela([@akx](https://github.com/akx)) wrote it as a little snack of sorts, but it may be useful for understanding
how to write very simple raw WSGI apps in Python. :)

https://github.com/akx/progressed.io-py

@akx:
> Unlike the original, the application itself will not bother with compressing the result, expecting
> it to be the duty of the the frontend HTTP server.

@akx:
> The source code fully conforms to PEP 8, aside from the SVG literal having an over-long line. :) 

This fork aims to improve its usability by parameterizing options, packaging the service...
and maintaining compatibility and improving its quality by adding CI

Usage:

* You may run `progressed.py` directly via Python, in which case it will bind the default Python
  `wsgiref.simple_server` server to 0.0.0.0:8080 and serve progress bars at `/bar/<progress>`.
* If you use uWSGI, `uwsgi --wsgi progressed --http 0.0.0.0:8080` should get you running.
