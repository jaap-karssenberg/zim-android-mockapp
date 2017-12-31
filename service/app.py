#!/usr/bin/python

import os
import urllib

class MockApp(object):

    def get_html(self, path):
        def start_response(response, headers):
            if not response.startswith('200'):
                raise AssertionError, response
            else:
                pass # Ignore all headers here

        return self.__call__({'PATH_INFO': path}, start_response)

    def __call__(self, environ, start_response):
        '''Main function for handling a single request. Follows the
        WSGI API.

        @param environ: dictionary with environment variables for the
        request and some special variables. See the PEP for expected
        variables.

        @param start_response: a function that can be called to set the
        http response and headers. For example::

            start_response(200, [('Content-Type', 'text/plain')])

        @returns: the html page content as a list of lines
        '''
        path = environ.get('PATH_INFO', '/')
        path = urllib.unquote(path)

        if path == '/':
            basename = 'index.html'
        else:
            if '/' in path:
                x, basename = path.rsplit('/', 1)
            else:
                basename = path

        pagespath = os.path.join(os.path.dirname(__file__), '..', 'pages')
        file = os.path.join(pagespath, basename)
        try:
            html = open(file).read()
        except:
            start_response('404 Not found', [])
            return ''
        else:
            start_response('200 OK', [('Content-Type', 'text/html; charset="utf-8"')])
            html = html.replace('</title>', '</title>\n<meta name="generator" content="MockApp">')
            return html


if __name__ == '__main__':
    import sys
    path = sys.argv[1]
    app = MockApp()
    print app.get_html(path)

