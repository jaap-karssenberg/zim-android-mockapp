#!/usr/bin/python

from gi.repository import WebKit
from gi.repository import Gtk

from app import MockApp

myapp = MockApp()
view = WebKit.WebView()

def load_page(path):
	html = myapp.get_html(path)
	view.load_html_string(html, path)


def overrule_navigation(view, frame, request, action, decision):
	if action.get_reason() == WebKit.WebNavigationReason.OTHER:
		pass
	else:
		# TODO: for internal links load the page, for external links load external app
		decision.ignore() # overrule
		load_page(request.get_uri())
		return True


view.connect('navigation-policy-decision-requested', overrule_navigation)


def close(window):
	Gtk.main_quit()

def main():
	Gtk.init()
	window = Gtk.Window()
	window.set_default_size(500, 500)
	swin = Gtk.ScrolledWindow()
	swin.add(view)
	window.add(swin)
	window.connect("destroy", close)
	window.show_all()
	Gtk.main()

load_page('/')
main()
