#!/usr/bin/python

import sys

from threading import Thread, Lock
import logging
import webview
from time import sleep
from server.main import run_server

server_lock = Lock()

logger = logging.getLogger(__name__)


def url_ok(url, port):
    # Use httplib on Python 2
    try:
        from http.client import HTTPConnection
    except ImportError:
        from httplib import HTTPConnection

    try:
        conn = HTTPConnection(url, port)
        conn.request("GET", "/")
        r = conn.getresponse()
        return r.status == 200
    except:
        logger.exception("Server not started")
        return False

def start_server():
    logger.debug("Starting server")
    t = Thread(target=run_server)
    t.daemon = True
    t.start()
    logger.debug("Checking server")

    while not url_ok("127.0.0.1", 23948):
        sleep(0.1)

    logger.debug("Server started")

def main():
    start_server()  # need to start the server as a thread ; in Android this is unnecessary as it will be started as a (background) service
    webview.create_window("ZimAndroid", "http://localhost:23948", min_size=(640, 480))  # this is a blocking command, nothing can be executed after! (or only in a thread launched before)

if __name__ == '__main__':
    main()