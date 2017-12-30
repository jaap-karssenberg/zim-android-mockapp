#!/usr/bin/python

print('ZIMDEBUGSERVICE')


# install_twisted_rector must be called before importing  and using the reactor
import os, sys

# For Android, install_twisted_rector must be called before importing  and using the reactor
#import sys
#if sys.platform == 'android' or sys.platform == 'linux3':  # linux3 for Bluestacks emulator
from kivy.support import install_twisted_reactor
install_twisted_reactor()

from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor, endpoints



from kivy.app import App
from kivy.uix.label import Label


class TwistedServerApp(App):
    def build(self):
        self.label = Label(text="server started\n")
        #reactor.listenTCP(23950, EchoFactory(self))
        resource = File(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pages"))
        factory = Site(resource)
        endpoint = endpoints.TCP4ServerEndpoint(reactor, 23950)
        endpoint.listen(factory)
        return self.label

    def handle_message(self, msg):
        self.label.text = "received:  %s\n" % msg

        if msg == "ping":
            msg = "pong"
        if msg == "plop":
            msg = "kivy rocks"
        self.label.text += "responded: %s\n" % msg
        return msg

    def getChild(self, name, request):
        if name == '':
            return self
        return resource.Resource.geChild(self, name, request)

    def render_GET(self, request):
        return "<html>Hello, world!</html>"


def run_server():
    TwistedServerApp().run()

if __name__ == '__main__':
    run_server()
