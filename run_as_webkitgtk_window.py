#!/usr/bin/python

import webview
from server.main import start_server

start_server()
#load_page(myapp, view, '/')
webview.create_window("ZimAndroid", "http://localhost:23948", min_size=(640, 480))  # this is a blocking command, nothing can be executed after! (or only in a thread launched before)
