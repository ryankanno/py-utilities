#!/usr/bin/env python
# -*- coding: utf-8 -*-

import BaseHTTPServer
import webbrowser


def browser(html, ip='127.0.0.1', port=0):
    class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        def do_GET(self):
            self.wfile.write(html)

    server = BaseHTTPServer.HTTPServer((ip, port), RequestHandler)
    webbrowser.open("http://{0}:{1}".format(*server.server_address))
    server.handle_request()

# vim: filetype=python
