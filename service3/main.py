#!/usr/bin/python

print('LALALALO')

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__)))

from waitress import serve

from app import MockApp

def run_server():
    print "Running server at http://localhost:23950"

    wsgiapp = MockApp()
    serve(wsgiapp, listen='0.0.0.0:23950')  # only on IPv4 to avoid crash on phones unsupporting IPv6

if __name__ == '__main__':
    run_server()
