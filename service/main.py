#!/usr/bin/python

print('ZIMDEBUGSERVICE')

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__)))

from wsgiref import simple_server

from app import MockApp

def run_server():
    print "Running server at http://localhost:23950"

    app = MockApp()
    httpd = simple_server.make_server('localhost', 23950, app)
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
