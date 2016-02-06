
from wsgiref import simple_server

from app import MockApp

print "Running server at http://localhost:8080"

app = MockApp()
httpd = simple_server.make_server('localhost', 8081, app)
httpd.serve_forever()
